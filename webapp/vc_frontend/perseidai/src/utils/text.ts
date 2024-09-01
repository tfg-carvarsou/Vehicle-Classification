export function updateText(selectedClass: string, newText: string): void {
  const element = document.querySelector(selectedClass);
  if (element) {
    element.textContent = newText;
  } else {
    console.warn(`Element with class "${selectedClass}" not found`);
  }
}