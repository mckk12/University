import { evaluate } from 'mathjs';

export function evaluateExpression(expr: string): string {
  return evaluate(expr).toString();
}