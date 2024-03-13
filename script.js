// Get the beam element and create a crack element
const beam = document.querySelector('.beam');
const crack = beam.querySelector('.crack');

// Define the distance threshold for the crack
const distanceThreshold = 100;

// Define a function to update the crack based on the distance
function updateCrack(distance) {
  if (distance <= distanceThreshold) {
    crack.style.display = 'block';
  } else {
    crack.style.display = 'none';
  }
}

// Example function to get distance from an ultrasonic sensor
function getDistance() {
  // Replace this with your own code to read sensor data
  return Math.floor(Math.random() * 200);
}

// Continuously update the crack based on sensor data
setInterval(() => {
  const distance = getDistance();
  updateCrack(distance);
}, 1000);

// Rotate the beam on mouse drag
let isDragging = false;
let previousMousePosition = {
  x: 0,
  y: 0,
};

beam.addEventListener('mousedown', (event) => {
  isDragging = true;
  previousMousePosition = {
    x: event.clientX,
    y: event.clientY,
  };
});

beam.addEventListener('mouseup', () => {
  isDragging = false;
});

beam.addEventListener('mousemove', (event) => {
  if (isDragging) {
    const delta = {
      x: event.clientX - previousMousePosition.x,
      y: event.clientY - previousMousePosition.y,
    };

    beam.style.transform = `rotateX(${delta.y}deg) rotateY(${delta.x}deg)`;
    previousMousePosition = {
      x: event.clientX,
      y: event.clientY,
    };
  }
});
 