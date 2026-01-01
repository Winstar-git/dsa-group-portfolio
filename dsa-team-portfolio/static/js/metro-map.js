// static/js/metro-map.js

let startStation = null;
let endStation = null;
const displayStart = document.getElementById('start_display');
const displayEnd = document.getElementById('end_display');
const inputStart = document.getElementById('start_input');
const inputEnd = document.getElementById('end_input');

document.querySelectorAll('.station-node').forEach(btn => {
  // Prevent clicking on sidebar buttons if you add any
  if(btn.closest('.control-panel')) return;

  btn.addEventListener('click', (e) => {
    e.preventDefault();
    const stationName = btn.dataset.name;
    
    // Gradients
    const defaultGradient = 'linear-gradient(135deg, #4f9dff 0%, #00bfff 100%)';
    const activeStart = 'linear-gradient(135deg, #00d4ff 0%, #00eaff 100%)'; 
    const activeEnd = 'linear-gradient(135deg, #005aff 0%, #0040ff 100%)'; 

    if (!startStation) {
      startStation = stationName;
      btn.style.background = activeStart;
      btn.style.transform = 'scale(1.15)';
      btn.style.boxShadow = '0 0 15px #00d4ff';
      displayStart.textContent = startStation;
      inputStart.value = startStation;
    } 
    else if (!endStation && stationName !== startStation) {
      endStation = stationName;
      btn.style.background = activeEnd;
      btn.style.transform = 'scale(1.15)';
      btn.style.boxShadow = '0 0 15px #004bff';
      displayEnd.textContent = endStation;
      inputEnd.value = endStation;
    } 
    else {
      // Reset
      startStation = stationName;
      endStation = null;

      displayStart.textContent = "None Selected";
      displayEnd.textContent = "None Selected";
      inputStart.value = "";
      inputEnd.value = "";

      // Visual Reset
      document.querySelectorAll('.station-node').forEach(b => {
         b.style.background = defaultGradient;
         b.style.transform = 'scale(1)';
         b.style.boxShadow = 'none';
      });

      // Select new start (effectively resetting to just having a start selected)
      btn.style.background = activeStart;
      btn.style.transform = 'scale(1.15)';
      btn.style.boxShadow = '0 0 15px #00d4ff';
      startStation = stationName;
      inputStart.value = startStation;
      displayStart.textContent = startStation;
    }
  });
});