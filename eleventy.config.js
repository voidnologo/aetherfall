module.exports = function (eleventyConfig) {

  // ── Passthrough: static assets that should not be processed ──
  eleventyConfig.addPassthroughCopy("web/rules/css");
  eleventyConfig.addPassthroughCopy("web/rules/js");
  eleventyConfig.addPassthroughCopy("web/rules/tools");
  eleventyConfig.addPassthroughCopy("web/assets");

  // ── Filter: look up a page and its neighbors from pages.json ──
  eleventyConfig.addFilter("pageNav", function (pages, pageId) {
    const idx = pages.findIndex(p => p.id === pageId);
    if (idx === -1) return { current: null, prev: null, next: null };
    return {
      current: pages[idx],
      prev: idx > 0 ? pages[idx - 1] : null,
      next: idx < pages.length - 1 ? pages[idx + 1] : null,
    };
  });

  // ── Filter: is a chapter number numeric (vs. special like "→" or "QS") ──
  eleventyConfig.addFilter("isNumbered", function (num) {
    return /^\d+$/.test(num);
  });

  // ── Voice callout shortcodes (fixed labels) ──
  const voiceCallouts = {
    handler:  { cls: "callout-handler",  label: "The Handler" },
    scholar:  { cls: "callout-scholar",  label: "The Scholar" },
    street:   { cls: "callout-street",   label: "The Street" },
    believer: { cls: "callout-believer", label: "The Believer" },
  };

  for (const [name, cfg] of Object.entries(voiceCallouts)) {
    eleventyConfig.addPairedShortcode(name, function (content) {
      return `<div class="callout ${cfg.cls}">\n  <span class="callout-label">${cfg.label}</span>\n${content}\n</div>`;
    });
  }

  // ── Utility callout shortcodes (custom labels with defaults) ──
  const utilityCallouts = {
    gmnote:  { cls: "callout-note",    defaultLabel: "For the GM" },
    example: { cls: "callout-example", defaultLabel: "At the Table" },
    warning: { cls: "callout-warning", defaultLabel: "Warning" },
    scene:   { cls: "callout-scene",   defaultLabel: "At the Table" },
  };

  for (const [name, cfg] of Object.entries(utilityCallouts)) {
    eleventyConfig.addPairedShortcode(name, function (content, label) {
      const lbl = label || cfg.defaultLabel;
      return `<div class="callout ${cfg.cls}">\n  <span class="callout-label">${lbl}</span>\n${content}\n</div>`;
    });
  }

  // ── Flat URLs: output rules/economy.html, not rules/economy/index.html ──
  eleventyConfig.addGlobalData("permalink", function () {
    return (data) => `${data.page.filePathStem}.html`;
  });

  return {
    dir: {
      input: "web",
      output: "_site",
      includes: "_includes",
      data: "_data",
    },
  };
};
