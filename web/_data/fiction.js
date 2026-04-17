const fs = require('fs');
const path = require('path');
const MarkdownIt = require('markdown-it');

const md = new MarkdownIt({
  html: false,
  linkify: false,
  typographer: false,
  breaks: false,
});

function renderChapter(raw) {
  const cleaned = raw
    .replace(/^#\s+Chapter\s+\d+\s*$/m, '')
    .trim();
  return md.render(cleaned);
}

function countWords(text) {
  return text.trim().split(/\s+/).length;
}

function loadStory02() {
  const dir = path.join(__dirname, '..', '..', 'fiction', 'stories', 'story-02');
  const chapters = [];
  const povOrder = ['Mira', 'Kael', 'Sera', 'Aldric', 'Mira', 'Sera', 'Kael', 'Aldric', 'Kael', 'Mira'];

  for (let i = 1; i <= 10; i++) {
    const file = path.join(dir, `ch${String(i).padStart(2, '0')}.md`);
    if (!fs.existsSync(file)) continue;
    const raw = fs.readFileSync(file, 'utf8');
    chapters.push({
      num: i,
      numDisplay: String(i).padStart(2, '0'),
      pov: povOrder[i - 1],
      words: countWords(raw),
      html: renderChapter(raw),
    });
  }

  const totalWords = chapters.reduce((a, c) => a + c.words, 0);
  const readMinutes = Math.round(totalWords / 240);
  const number = 2;

  return {
    slug: 'what-the-mill-remembered',
    number,
    numberDisplay: String(number).padStart(2, '0'),
    wordsDisplay: totalWords.toLocaleString('en-US'),
    title: 'What the Mill Remembered',
    subtitle: 'A Tale of the Ash & Veil Society',
    blurb: 'A rushed patron job sends a young Society into the Wilds northeast of Ashwick, hunting an artifact rumored inside a pre-Tear mill whose interior has been remade into something the builders would not recognize — and they are not the only ones looking.',
    tagline: 'A short story of the Ash & Veil Society',
    location: 'Ashwick &mdash; and the Wilds beyond',
    tone: 'Propulsive, wonder-threaded, dark at the edges',
    totalWords,
    readMinutes,
    chapters,
  };
}

module.exports = function () {
  const story02 = loadStory02();
  return {
    stories: [story02],
    storiesBySlug: { [story02.slug]: story02 },
  };
};
