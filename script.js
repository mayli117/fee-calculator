
async function uploadFile(file) {
  const formData = new FormData();
  formData.append("file", file);
  const res = await fetch("https://github.com/mayli117/fee-calculator.vercel.app/upload", {
    method: "POST",
    body: formData
  });
  return await res.json();
}

async function calculate() {
  const start = document.getElementById("startDate").value;
  const end = document.getElementById("endDate").value;
  const cycle = parseInt(document.getElementById("cycle").value);
  const oldRent = parseFloat(document.getElementById("oldRent").value);
  const newRent = parseFloat(document.getElementById("newRent").value);
  const packageTotal = parseFloat(document.getElementById("package").value);

  const payload = {
    start_date: start,
    end_date: end,
    cycle: cycle,
    rent: oldRent
  };

  const res = await fetch("https://github.com/mayli117/fee-calculator.vercel.app/calculate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const result = await res.json();
  document.getElementById("result").value = `
起始日：${start}
終止日：${end}
使用日數：${result.total_days} 天
總費用：${result.total_fee} 元
`;
}

function copyResult() {
  const text = document.getElementById("result");
  text.select();
  document.execCommand("copy");
  alert("已複製結果！");
}

