const root = document.documentElement;
document.querySelector('.theme-toggle')?.addEventListener('click', () => {
  const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
  root.dataset.theme = next;
  localStorage.setItem('theme', next);
});
const search = document.querySelector('#course-search');
search?.addEventListener('input', () => {
  const query = search.value.trim().toLocaleLowerCase('ko');
  document.querySelectorAll('.course-card').forEach((card) => {
    card.hidden = !card.dataset.search.toLocaleLowerCase('ko').includes(query);
  });
  document.querySelectorAll('.semester').forEach((term) => {
    term.hidden = !term.querySelector('.course-card:not([hidden])');
  });
});
const prose = document.querySelector('.note-layout .prose');
const toc = document.querySelector('.toc');
if (prose && toc) {
  const headings = [...prose.querySelectorAll('h2, h3')];
  headings.forEach((heading, index) => {
    if (!heading.id) heading.id = `section-${index + 1}`;
    const link = document.createElement('a');
    link.href = `#${heading.id}`;
    link.textContent = heading.textContent;
    link.className = heading.tagName === 'H3' ? 'toc-sub' : '';
    toc.appendChild(link);
  });
  if (!headings.length) toc.hidden = true;
  document.querySelector('.toc-toggle')?.addEventListener('click', () => toc.classList.toggle('open'));
}
