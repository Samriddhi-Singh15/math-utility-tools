function addFraction() {
  const frac1 = document.getElementById("frac1").value;
  const frac2 = document.getElementById("frac2").value;
  const result = calculateFractionSum(frac1, frac2);
  document.getElementById("frac-result").innerText = "Result: " + result;
}

function calculateFractionSum(f1, f2) {
  const [n1, d1] = f1.split("/").map(Number);
  const [n2, d2] = f2.split("/").map(Number);
  const num = n1 * d2 + n2 * d1;
  const denom = d1 * d2;
  const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));
  const divisor = gcd(num, denom);
  return `${num / divisor}/${denom / divisor}`;
}

function subtractFraction() {
  const frac1 = document.getElementById("frac1").value;
  const frac2 = document.getElementById("frac2").value;

  const result = calculateFractionDiff(frac1, frac2);
  document.getElementById("frac-result").innerText = "Result: " + result;
}

function calculateFractionDiff(f1, f2) {
  const [n1, d1] = f1.split("/").map(Number);
  const [n2, d2] = f2.split("/").map(Number);

  const commonDenom = d1 * d2;
  const num = n1 * d2 - n2 * d1;

  const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));
  const divisor = gcd(num, commonDenom);

  return `${num / divisor}/${commonDenom / divisor}`;
}

function multiplyFraction() {
  const frac1 = document.getElementById("frac1").value;
  const frac2 = document.getElementById("frac2").value;
  const result = calculateFractionProduct(frac1, frac2);
  document.getElementById("frac-result").innerText = "Result: " + result;
}

function calculateFractionProduct(f1, f2) {
  const [n1, d1] = f1.split("/").map(Number);
  const [n2, d2] = f2.split("/").map(Number);
  const num = n1 * n2;
  const denom = d1 * d2;
  const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));
  const divisor = gcd(num, denom);
  return `${num / divisor}/${denom / divisor}`;
}

function divideFraction() {
  const frac1 = document.getElementById("frac1").value;
  const frac2 = document.getElementById("frac2").value;
  const result = calculateFractionQuotient(frac1, frac2);
  document.getElementById("frac-result").innerText = "Result: " + result;
}

function calculateFractionQuotient(f1, f2) {
  const [n1, d1] = f1.split("/").map(Number);
  const [n2, d2] = f2.split("/").map(Number);
  const num = n1 * d2;
  const denom = d1 * n2;
  const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));
  const divisor = gcd(num, denom);
  return `${num / divisor}/${denom / divisor}`;
}

function convertToDecimal() {
  const frac = document.getElementById("single-frac").value;
  const [num, denom] = frac.split("/").map(Number);
  const result = num / denom;
  document.getElementById("single-frac-result").innerText = "Decimal: " + result.toFixed(5);
}

function simplifyFraction() {
  const frac = document.getElementById("simplify-frac").value;
  const [num, denom] = frac.split("/").map(Number);
  const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));
  const divisor = gcd(num, denom);
  const simple = `${num / divisor}/${denom / divisor}`;
  document.getElementById("simplify-result").innerText = "Simplified: " + simple;
}

function mixedToImproper() {
  const input = document.getElementById("mixed-frac").value;
  const [whole, frac] = input.split(" ");
  const [num, denom] = frac.split("/").map(Number);
  const improper = `${(Number(whole) * denom + num)}/${denom}`;
  document.getElementById("mixed-improper-result").innerText = "Improper: " + improper;
}

function improperToMixed() {
  const input = document.getElementById("improper-frac").value;
  const [num, denom] = input.split("/").map(Number);
  const whole = Math.floor(num / denom);
  const remainder = num % denom;
  const mixed = remainder === 0 ? `${whole}` : `${whole} ${remainder}/${denom}`;
  document.getElementById("improper-mixed-result").innerText = "Mixed: " + mixed;
}

function floatConversion() {
  const frac = document.getElementById("float-frac").value;
  const [num, denom] = frac.split("/").map(Number);
  const result = num / denom;
  document.getElementById("float-result").innerText = "Float: " + result.toFixed(5);
}
function calculateEuclideanDistance(){
  const x1=parseFloat(document.getElementById("x1").value);
  const y1=parseFloat(document.getElementById("y1").value);
  const x2=parseFloat(document.getElementById("x2").value);
  const y2=parseFloat(document.getElementById("y2").value);

  const dx=x2-x1;
  const dy=y2-y1;

  const distance=Math.sqrt(dx*dx + dy*dy).toFixed(4);

  document.getElementById("euclidean-result").innerText="Distance: "+distance;
}
function distanceFromOrigin(){
  const x=parseFloat(document.getElementById("origin-x").value);
  const y=parseFloat(document.getElementById("origin-y").value);

  const distance=Math.sqrt(x*x+y*y);

  document.getElementById("origin-result").innerText="Distance from Origin: "+distance;
}
function findMidpoint(){
  const x1=parseFloat(document.getElementById("mid-x1").value);
  const y1=parseFloat(document.getElementById("mid-y1").value);
  const x2=parseFloat(document.getElementById("mid-x2").value);
  const y2=parseFloat(document.getElementById("mid-y2").value);

  const midX=((x1+x2)/2).toFixed(2);
  const midY=((y1+y2)/2).toFixed(2);

  document.getElementById("midpoint-result").innerText = `Midpoint: (${midX}, ${midY})`;
}
function calculateSlope(){
  const x1=parseFloat(document.getElementById("slope-x1").value);
  const y1=parseFloat(document.getElementById("slope-y1").value);
  const x2=parseFloat(document.getElementById("slope-x2").value);
  const y2=parseFloat(document.getElementById("slope-y2").value);

  if(x2===x1){
      document.getElementById("slope-result").innerText="Slope: Underdefined(vertical line)";
      return;
  }

  const slope=((y2-y1)/(x2-x1)).toFixed(3);
  document.getElementById("slope-result").innerText="Slope: "+slope;
}
function findQuadrant() {
  const x = parseFloat(document.getElementById("quad-x").value);
  const y = parseFloat(document.getElementById("quad-y").value);

  let result = "";

  if (x === 0 && y === 0) result = "Origin";
  else if (x === 0) result = "On Y-axis";
  else if (y === 0) result = "On X-axis";
  else if (x > 0 && y > 0) result = "Quadrant I";
  else if (x < 0 && y > 0) result = "Quadrant II";
  else if (x < 0 && y < 0) result = "Quadrant III";
  else if (x > 0 && y < 0) result = "Quadrant IV";

  document.getElementById("quad-result").innerText = "Location: " + result;
}
function lineSlope() {
  const A = parseFloat(document.getElementById("line-A").value);
  const B = parseFloat(document.getElementById("line-B").value);

  if (B === 0) {
    document.getElementById("line-slope-result").innerText = "Slope: Undefined (horizontal line)";
    return;
  }

  const slope = (-A / B).toFixed(3);
  document.getElementById("line-slope-result").innerText = "Slope: " + slope;
}
function yIntercept() {
  const B = parseFloat(document.getElementById("intercept-B").value);
  const C = parseFloat(document.getElementById("intercept-C").value);

  if (B === 0) {
    document.getElementById("y-intercept-result").innerText = "Y-Intercept: Undefined";
    return;
  }

  const yInt = (-C / B).toFixed(3);
  document.getElementById("y-intercept-result").innerText = "Y-Intercept: " + yInt;
}
function lineFromTwoPoints() {
  const x1 = parseFloat(document.getElementById("line-x1").value);
  const y1 = parseFloat(document.getElementById("line-y1").value);
  const x2 = parseFloat(document.getElementById("line-x2").value);
  const y2 = parseFloat(document.getElementById("line-y2").value);

  if (x1 === x2) {
    document.getElementById("line-equation-result").innerText = "Line: x = " + x1;
    return;
  }

  const m = (y2 - y1) / (x2 - x1);
  const c = y1 - m * x1;

  const mRounded = m.toFixed(2);
  const cRounded = c.toFixed(2);

  document.getElementById("line-equation-result").innerText = `Line: y = ${mRounded}x + ${cRounded}`;
}
function isPointOnLine() {
  const A = parseFloat(document.getElementById("check-A").value);
  const B = parseFloat(document.getElementById("check-B").value);
  const C = parseFloat(document.getElementById("check-C").value);
  const x = parseFloat(document.getElementById("check-x").value);
  const y = parseFloat(document.getElementById("check-y").value);

  const result = A * x + B * y + C;

  const message = result === 0 ? "✅ Point lies on the line" : "❌ Point does NOT lie on the line";

  document.getElementById("point-line-result").innerText = message;
}
function shortestDistanceToLine() {
  const A = parseFloat(document.getElementById("dist-A").value);
  const B = parseFloat(document.getElementById("dist-B").value);
  const C = parseFloat(document.getElementById("dist-C").value);
  const x = parseFloat(document.getElementById("dist-x").value);
  const y = parseFloat(document.getElementById("dist-y").value);

  const numerator = Math.abs(A * x + B * y + C);
  const denominator = Math.sqrt(A * A + B * B);

  const distance = (numerator / denominator).toFixed(4);

  document.getElementById("point-line-dist-result").innerText = "Distance: " + distance;
}
function addPoly() {
  const p1 = document.getElementById("poly-add-1").value.split(",").map(Number);
  const p2 = document.getElementById("poly-add-2").value.split(",").map(Number);

  const maxLen = Math.max(p1.length, p2.length);
  const result = [];

  for (let i = 0; i < maxLen; i++) {
    const a = p1[p1.length - 1 - i] || 0;
    const b = p2[p2.length - 1 - i] || 0;
    result.unshift(a + b);
  }

  document.getElementById("poly-add-result").innerText = "Result: " + result.join(", ");
}
function subtractPoly() {
  const p1 = document.getElementById("poly-sub-1").value.split(",").map(Number);
  const p2 = document.getElementById("poly-sub-2").value.split(",").map(Number);

  const maxLen = Math.max(p1.length, p2.length);
  const result = [];

  for (let i = 0; i < maxLen; i++) {
    const a = p1[p1.length - 1 - i] || 0;
    const b = p2[p2.length - 1 - i] || 0;
    result.unshift(a - b);
  }

  document.getElementById("poly-sub-result").innerText = "Result: " + result.join(", ");
}
function multiplyPoly() {
  const p1 = document.getElementById("poly-mul-1").value.split(",").map(Number);
  const p2 = document.getElementById("poly-mul-2").value.split(",").map(Number);

  const result = Array(p1.length + p2.length - 1).fill(0);

  for (let i = 0; i < p1.length; i++) {
    for (let j = 0; j < p2.length; j++) {
      result[i + j] += p1[i] * p2[j];
    }
  }

  document.getElementById("poly-mul-result").innerText = "Result: " + result.join(", ");
}
function dividePoly() {
  const p1 = document.getElementById("poly-div-1").value.split(",").map(Number);
  const p2 = document.getElementById("poly-div-2").value.split(",").map(Number);

  document.getElementById("poly-div-result").innerText = `Send to backend for division: \nP1 = [${p1}], P2 = [${p2}]`;
}