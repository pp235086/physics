// ฟังก์ชันสำหรับคำนวณแรงดันไฟฟ้า
function calculateVoltage() {
  const current = parseFloat(document.getElementById("current").value);
  const resistance = parseFloat(document.getElementById("resistance").value);

  if (isNaN(current) || isNaN(resistance)) {
    document.getElementById("result").innerText = "Please enter valid numbers!";
    return;
  }

  const voltage = current * resistance;
  document.getElementById("result").innerText = Voltage (V): ${voltage.toFixed(2)} V;
}
