#!/usr/bin/env python3
"""
Convert standalone tool HTML pages to Hugo content pages.
Extracts tool-specific CSS, HTML body, and JS from each static tool page
and creates Hugo-compatible content files that use baseof.html for the shared shell.
"""
import os
import re
import html as html_mod

TOOLS_DIR = os.path.join(os.path.dirname(__file__), '..', 'static', 'tools')
CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', 'content', 'tools')

# CSS section headers that should be REMOVED (handled by baseof.html)
REMOVE_SECTIONS = [
    'HEADER & MEGA-MENU',
    'HEADER',
    'MEGA-MENU',
    'FOOTER',
]

# CSS section headers that should be KEPT (tool-specific)
KEEP_SECTIONS = [
    'HERO',
    'LAYOUT',
    'CARD',
    'FORM',
    'RESULTS',
    'SIDEBAR',
    'SEO',
    'RESPONSIVE',
    'STEP',
    'WIZARD',
    'COMPARISON',
    'BANK',
    'INSURANCE',
    'TOOL',
    'OPTION',
    'RESULT',
    'ACCORDION',
    'TIMELINE',
    'STATUS',
    'TIP',
    'CTA',
    'SCORE',
    'BADGE',
    'CHECKLIST',
    'TABLE',
    'DATA',
    'BREAKDOWN',
    'DISCLAIMER',
    'PERMIT',
    'RECOMMENDATION',
    'PATHWAY',
    'Print',
]


def extract_title(html_content):
    m = re.search(r'<title>([^<]+)</title>', html_content)
    if m:
        title = m.group(1).split('—')[0].split('|')[0].strip()
        title = html_mod.unescape(title).replace('&mdash;', '—').strip()
        return title
    return "Tool"


def extract_description(html_content):
    m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html_content)
    if m:
        return html_mod.unescape(m.group(1))
    return ""


def extract_jsonld(html_content):
    """Extract JSON-LD blocks (for WebApplication, FAQPage etc.)"""
    blocks = re.findall(
        r'<script\s+type="application/ld\+json">\s*(.*?)\s*</script>',
        html_content, re.DOTALL
    )
    result = []
    for block in blocks:
        # Skip BreadcrumbList (baseof.html handles this)
        if '"BreadcrumbList"' in block:
            continue
        result.append(block.strip())
    return result


def extract_tool_css(html_content):
    """Extract CSS from <style> block, keeping only tool-specific sections"""
    m = re.search(r'<style>(.*?)</style>', html_content, re.DOTALL)
    if not m:
        return ""

    css = m.group(1)

    # Split CSS into sections using the comment delimiter pattern
    # Pattern: /* === SECTION NAME === */
    section_headers = re.findall(r'/\*\s*=+\s*\n?\s*[A-Z].*?\n?\s*=+\s*\*/', css)

    if section_headers:
        # Has section comments — use section-based splitting
        sections = re.split(
            r'(/\*\s*=+\s*\n?\s*[A-Z].*?\n?\s*=+\s*\*/)',
            css
        )

        result_parts = []
        skip_next = False
        i = 0
        while i < len(sections):
            part = sections[i]

            header_match = re.search(r'/\*\s*=+\s*\n?\s*(.*?)\s*\n?\s*=+\s*\*/', part)
            if header_match:
                section_name = header_match.group(1).strip()
                should_remove = any(rm.upper() in section_name.upper() for rm in REMOVE_SECTIONS)

                if should_remove:
                    skip_next = True
                else:
                    result_parts.append(part)
                    skip_next = False
            else:
                if not skip_next:
                    if i == 0:
                        # Everything before first section comment — remove shared CSS
                        pass
                    else:
                        result_parts.append(part)
                skip_next = False

            i += 1

        css_result = ''.join(result_parts).strip()
    else:
        # No section comments — use the full CSS and rely on regex cleanup
        css_result = css.strip()

    # Remove any leftover header/nav/footer rules that weren't in sections
    # (some tools inline these without section comments)
    shared_selectors = [
        r'#nav-toggle\s*\{[^}]+\}',
        r'header\s*\{[^}]+\}',
        r'\.header-inner\s*\{[^}]+\}',
        r'\.logo(?:\s*\{[^}]+\}|:hover\s*\{[^}]+\})',
        r'\.logo-(?:icon|text)(?:\s+span)?\s*\{[^}]+\}',
        r'\.primary-nav\s*\{[^}]+\}',
        r'\.nav-item[^{]*\{[^}]+\}',
        r'\.mega-[^{]*\{[^}]+\}',
        r'\.city-pill[^{]*\{[^}]+\}',
        r'\.header-cta[^{]*\{[^}]+\}',
        r'\.hamburger-label[^{]*\{[^}]+\}',
        r'#nav-toggle:checked[^{]*\{[^}]+\}',
        r'\.mobile-nav[^{]*\{[^}]+\}',
        r'\.site-footer[^{]*\{[^}]+\}',
        r'\.footer-(?:inner|grid|col-title|bottom|disclosure|links-bottom)[^{]*\{[^}]+\}',
    ]
    for pat in shared_selectors:
        css_result = re.sub(pat, '', css_result)

    # Remove the 768px media query content that only deals with nav
    def clean_768_query(match):
        content = match.group(1)
        # Remove nav-related rules
        nav_patterns = [
            r'\.primary-nav[^}]+\}',
            r'\.header-cta[^}]+\}',
            r'\.hamburger-label[^}]+\}',
            r'\.mega-menu[^}]+\}',
        ]
        for np in nav_patterns:
            content = re.sub(np, '', content)

        content = content.strip()
        if not content or all(c in ' \n\t{},' for c in content):
            return ''
        return f'@media (max-width: 768px) {{\n{content}\n    }}'

    css_result = re.sub(
        r'@media\s*\(max-width:\s*768px\)\s*\{(.*?)\n\s*\}',
        clean_768_query, css_result, flags=re.DOTALL
    )

    # Clean up print media query
    css_result = re.sub(
        r'@media\s+print\s*\{.*?\n\s*\}',
        '', css_result, flags=re.DOTALL
    )

    # Clean up excessive whitespace
    css_result = re.sub(r'\n{3,}', '\n\n', css_result)
    css_result = css_result.strip()

    return css_result


def extract_body(html_content):
    """Extract the tool body HTML between header and footer"""
    # Find content after </header>
    header_end = html_content.find('</header>')
    if header_end == -1:
        return ""
    body_start = header_end + len('</header>')

    # Find footer start
    footer_patterns = [
        '<!-- FOOTER -->',
        '<footer class="site-footer">',
        '<footer>',
    ]
    footer_start = len(html_content)
    for fp in footer_patterns:
        idx = html_content.find(fp, body_start)
        if idx != -1 and idx < footer_start:
            footer_start = idx

    body = html_content[body_start:footer_start].strip()

    # Replace <main class="page-body"> with <div class="page-body">
    body = re.sub(r'<main\s+class="page-body">', '<div class="page-body">', body)
    body = body.replace('</main>', '</div>')

    return body


def extract_js(html_content):
    """Extract tool-specific JavaScript (not GA4/cookie scripts)"""
    # Find scripts after the header/before footer
    header_end = html_content.find('</header>')
    if header_end == -1:
        header_end = 0

    scripts = re.findall(r'<script>(.*?)</script>', html_content[header_end:], re.DOTALL)
    result = []
    for script in scripts:
        script = script.strip()
        # Skip short GA4/cookie-only scripts (< 500 chars)
        # Long scripts that happen to contain gtag event calls are tool scripts
        if len(script) < 500:
            if any(skip in script for skip in [
                'googletagmanager',
                'gtag(',
                'dataLayer',
                'cookieConsent',
                'cookie-consent',
                'cookieBanner',
                'acceptCookies',
                'declineCookies',
            ]):
                continue
        if len(script) > 100:
            result.append(script)
    return result


def convert_tool(tool_dir, tool_name):
    """Convert a single tool from static HTML to Hugo content"""
    html_path = os.path.join(tool_dir, 'index.html')
    if not os.path.exists(html_path):
        print(f"  SKIP: {html_path} not found")
        return False

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    title = extract_title(content)
    description = extract_description(content)
    jsonld_blocks = extract_jsonld(content)
    css = extract_tool_css(content)
    body = extract_body(content)
    js_blocks = extract_js(content)

    if not body:
        print(f"  ERROR: Could not extract body from {tool_name}")
        return False

    # Escape any Hugo template delimiters in the content
    # (shouldn't be any, but just in case)

    # Build the Hugo content
    # Escape quotes in title/description for YAML
    safe_title = title.replace('"', '\\"')
    safe_desc = description.replace('"', '\\"')

    md = f'''---
title: "{safe_title}"
description: "{safe_desc}"
type: "tools"
layout: "single"
---

'''

    # Add JSON-LD schemas
    for block in jsonld_blocks:
        md += f'<script type="application/ld+json">\n{block}\n</script>\n\n'

    # Add tool-specific CSS
    if css:
        md += f'<style>\n{css}\n</style>\n\n'

    # Strip leading indentation from body HTML to prevent CommonMark
    # from treating 4+ space indented lines as code blocks
    body_lines = body.split('\n')
    body = '\n'.join(
        '' if line.strip() == '' else line.lstrip()
        for line in body_lines
    )

    # Add body
    md += body + '\n'

    # Add JS
    for js in js_blocks:
        md += f'\n<script>\n{js}\n</script>\n'

    # Write content file
    content_dir = os.path.join(CONTENT_DIR, tool_name)
    os.makedirs(content_dir, exist_ok=True)
    content_path = os.path.join(content_dir, 'index.md')

    with open(content_path, 'w', encoding='utf-8') as f:
        f.write(md)

    print(f"  OK: {tool_name} -> content/tools/{tool_name}/index.md "
          f"({len(md)} bytes, CSS: {len(css)}, JS blocks: {len(js_blocks)})")
    return True


def main():
    os.makedirs(CONTENT_DIR, exist_ok=True)

    # Ensure _index.md exists for the tools section
    index_path = os.path.join(CONTENT_DIR, '_index.md')
    if not os.path.exists(index_path):
        with open(index_path, 'w') as f:
            f.write(
                '---\n'
                'title: "Free Expat Tools Netherlands 2026"\n'
                'description: "11 free interactive tools for expats in the '
                'Netherlands: salary calculator, health insurance comparison, '
                'visa check, rent affordability calculator, and more."\n'
                'type: "tools"\n'
                'layout: "list"\n'
                '---\n'
            )

    # Get all tool directories
    tools = []
    for item in sorted(os.listdir(TOOLS_DIR)):
        tool_dir = os.path.join(TOOLS_DIR, item)
        if os.path.isdir(tool_dir) and os.path.exists(
            os.path.join(tool_dir, 'index.html')
        ):
            tools.append((tool_dir, item))

    print(f"Found {len(tools)} tools to convert:\n")

    converted = 0
    for tool_dir, tool_name in tools:
        print(f"Converting: {tool_name}")
        if convert_tool(tool_dir, tool_name):
            converted += 1

    print(f"\n{'='*60}")
    print(f"Converted {converted}/{len(tools)} tools successfully")


if __name__ == '__main__':
    main()
