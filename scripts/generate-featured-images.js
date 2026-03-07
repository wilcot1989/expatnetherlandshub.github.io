const fs = require('fs');
const path = require('path');
const sharp = require('sharp');
const { createCanvas, GlobalFonts } = require('@napi-rs/canvas');

// Category colors — maps all used categories to brand colors
const CATEGORY_COLORS = {
  'finance':      { bg: '#1B6B4A', label: 'Finance & Tax' },
  'health':       { bg: '#2563EB', label: 'Health' },
  'housing':      { bg: '#E8832A', label: 'Housing' },
  'legal':        { bg: '#7C3AED', label: 'Legal' },
  'work':         { bg: '#0891B2', label: 'Work & Career' },
  'integration':  { bg: '#DC2626', label: 'Integration' },
  'daily-life':   { bg: '#4F46E5', label: 'Daily Life' },
  'relocation':   { bg: '#7C3AED', label: 'Relocation' },
  'language':     { bg: '#DC2626', label: 'Language' },
  'insurance':    { bg: '#2563EB', label: 'Insurance' },
  'lifestyle':    { bg: '#4F46E5', label: 'Lifestyle' },
  'culture':      { bg: '#DC2626', label: 'Culture' },
  'family':       { bg: '#E8832A', label: 'Family' },
  'transport':    { bg: '#0891B2', label: 'Transport' },
  'career':       { bg: '#0891B2', label: 'Career' },
};

const DEFAULT_COLOR = { bg: '#1B6B4A', label: 'Guide' };

const WIDTH = 1200;
const HEIGHT = 630;
const PADDING = 60;

const CONTENT_DIR = path.join(__dirname, '..', 'content');
const OUTPUT_DIR = path.join(__dirname, '..', 'static', 'images', 'featured');

function parseFrontMatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return null;

  const fm = {};
  const lines = match[1].split('\n');
  for (const line of lines) {
    const titleMatch = line.match(/^title:\s*"(.+)"/);
    if (titleMatch) fm.title = titleMatch[1];

    const catMatch = line.match(/^categories:\s*\["(.+?)"\]/);
    if (catMatch) fm.category = catMatch[1];
  }
  return fm;
}

function wrapText(ctx, text, maxWidth) {
  const words = text.split(' ');
  const lines = [];
  let currentLine = '';

  for (const word of words) {
    const testLine = currentLine ? `${currentLine} ${word}` : word;
    const metrics = ctx.measureText(testLine);
    if (metrics.width > maxWidth && currentLine) {
      lines.push(currentLine);
      currentLine = word;
    } else {
      currentLine = testLine;
    }
  }
  if (currentLine) lines.push(currentLine);
  return lines;
}

function findFontSize(ctx, text, maxWidth, maxLines, startSize, minSize) {
  for (let size = startSize; size >= minSize; size -= 2) {
    ctx.font = `bold ${size}px sans-serif`;
    const lines = wrapText(ctx, text, maxWidth);
    if (lines.length <= maxLines) return { size, lines };
  }
  ctx.font = `bold ${minSize}px sans-serif`;
  const lines = wrapText(ctx, text, maxWidth);
  return { size: minSize, lines: lines.slice(0, maxLines) };
}

function hexToRgb(hex) {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return { r, g, b };
}

function generateImage(title, category, slug) {
  const catInfo = CATEGORY_COLORS[category] || DEFAULT_COLOR;
  const { bg, label } = catInfo;
  const { r, g, b } = hexToRgb(bg);

  const canvas = createCanvas(WIDTH, HEIGHT);
  const ctx = canvas.getContext('2d');

  // Background gradient (darker at bottom)
  const gradient = ctx.createLinearGradient(0, 0, 0, HEIGHT);
  gradient.addColorStop(0, bg);
  gradient.addColorStop(1, `rgb(${Math.max(0, r - 30)}, ${Math.max(0, g - 30)}, ${Math.max(0, b - 30)})`);
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, WIDTH, HEIGHT);

  // Subtle pattern — diagonal lines for texture
  ctx.strokeStyle = `rgba(255, 255, 255, 0.05)`;
  ctx.lineWidth = 1;
  for (let i = -HEIGHT; i < WIDTH + HEIGHT; i += 40) {
    ctx.beginPath();
    ctx.moveTo(i, 0);
    ctx.lineTo(i + HEIGHT, HEIGHT);
    ctx.stroke();
  }

  // Top accent bar
  ctx.fillStyle = 'rgba(255, 255, 255, 0.15)';
  ctx.fillRect(0, 0, WIDTH, 6);

  // Category pill
  ctx.font = 'bold 18px sans-serif';
  const pillText = label.toUpperCase();
  const pillMetrics = ctx.measureText(pillText);
  const pillWidth = pillMetrics.width + 32;
  const pillHeight = 36;
  const pillX = PADDING;
  const pillY = PADDING + 10;

  ctx.fillStyle = 'rgba(255, 255, 255, 0.2)';
  ctx.beginPath();
  ctx.roundRect(pillX, pillY, pillWidth, pillHeight, 18);
  ctx.fill();

  ctx.fillStyle = '#ffffff';
  ctx.fillText(pillText, pillX + 16, pillY + 24);

  // Title
  const maxWidth = WIDTH - PADDING * 2;
  const { size, lines } = findFontSize(ctx, title, maxWidth, 3, 52, 30);
  ctx.font = `bold ${size}px sans-serif`;
  ctx.fillStyle = '#ffffff';

  const lineHeight = size * 1.25;
  const titleStartY = pillY + pillHeight + 50;

  for (let i = 0; i < lines.length; i++) {
    ctx.fillText(lines[i], PADDING, titleStartY + i * lineHeight);
  }

  // Bottom section — site name + decorative line
  const bottomY = HEIGHT - PADDING - 10;

  // Decorative line
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(PADDING, bottomY - 30);
  ctx.lineTo(WIDTH - PADDING, bottomY - 30);
  ctx.stroke();

  // Site name
  ctx.font = 'bold 20px sans-serif';
  ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
  ctx.fillText('expatnetherlandshub.com', PADDING, bottomY);

  // Year badge
  ctx.font = 'bold 20px sans-serif';
  const yearText = '2026';
  const yearMetrics = ctx.measureText(yearText);
  ctx.fillText(yearText, WIDTH - PADDING - yearMetrics.width, bottomY);

  // NL flag colors accent (bottom-right corner)
  const flagWidth = 60;
  const flagHeight = 4;
  const flagY = HEIGHT - flagHeight;
  // Red
  ctx.fillStyle = '#AE1C28';
  ctx.fillRect(WIDTH - flagWidth * 3, flagY, flagWidth, flagHeight);
  // White
  ctx.fillStyle = '#FFFFFF';
  ctx.fillRect(WIDTH - flagWidth * 2, flagY, flagWidth, flagHeight);
  // Blue
  ctx.fillStyle = '#21468B';
  ctx.fillRect(WIDTH - flagWidth, flagY, flagWidth, flagHeight);

  return canvas.toBuffer('image/png');
}

async function processFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const fm = parseFrontMatter(content);
  if (!fm || !fm.title) return null;

  const slug = path.basename(filePath, '.md');
  const category = fm.category || 'daily-life';

  // Generate PNG buffer from canvas
  const pngBuffer = generateImage(fm.title, category, slug);

  // Convert to WebP with Sharp
  const outputPath = path.join(OUTPUT_DIR, `${slug}.webp`);
  await sharp(pngBuffer)
    .webp({ quality: 85 })
    .toFile(outputPath);

  return { slug, title: fm.title, category, outputPath };
}

async function updateFrontMatter(filePath, slug) {
  let content = fs.readFileSync(filePath, 'utf-8');
  const featuredImage = `/images/featured/${slug}.webp`;

  // Check if featured_image already exists
  if (content.includes('featured_image:')) {
    content = content.replace(/featured_image:.*/, `featured_image: "${featuredImage}"`);
  } else {
    // Add after the last front matter field before ---
    content = content.replace(/\n---\n/, `\nfeatured_image: "${featuredImage}"\n---\n`);
  }

  fs.writeFileSync(filePath, content, 'utf-8');
}

async function main() {
  // Ensure output dir exists
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  // Find all .md files (not _index.md)
  const files = [];
  function walk(dir) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(fullPath);
      } else if (entry.name.endsWith('.md') && entry.name !== '_index.md') {
        files.push(fullPath);
      }
    }
  }
  walk(CONTENT_DIR);

  console.log(`Found ${files.length} content files`);

  let generated = 0;
  let errors = 0;

  for (const filePath of files) {
    try {
      const result = await processFile(filePath);
      if (result) {
        await updateFrontMatter(filePath, result.slug);
        generated++;
        console.log(`  [OK] ${result.slug} (${result.category})`);
      }
    } catch (err) {
      errors++;
      console.error(`  [ERR] ${path.basename(filePath)}: ${err.message}`);
    }
  }

  console.log(`\nDone: ${generated} images generated, ${errors} errors`);
}

main().catch(console.error);
