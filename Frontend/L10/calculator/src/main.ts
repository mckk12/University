import { evaluateExpression } from './calculator';

const display = document.getElementById('display') as HTMLInputElement;
const buttons = document.querySelectorAll('button[data-value]');

buttons.forEach(btn => {
  btn.addEventListener('click', () => {
    if (display.value === 'Error') {
      display.value = '';
    }
    display.value += (btn as HTMLButtonElement).dataset.value || '';
  });
});

document.getElementById('clear')?.addEventListener('click', () => {
  display.value = '';
});

document.getElementById('back')?.addEventListener('click', () => {
  display.value = display.value.slice(0, -1);
});

document.getElementById('equals')?.addEventListener('click', () => {
  try {
    const result:string = evaluateExpression(display.value);
    if (result === 'NaN' || result === 'Infinity'){
      throw new Error('Invalid result');
    }
    display.value = result;
  } catch {
    display.value = 'Error';
  }
});
