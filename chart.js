let demo = document.getElementById("chat-container");
let outputContainer = document.getElementById("output-container");

demo.addEventListener("submit", (e) => {
  e.preventDefault();
  let userInput = document.getElementById("user-input").value.trim();

  if (userInput === '') {
    return;
  }

  showLoadingAnimation();

  fetch('http://127.0.0.1:8000/demo/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      question: userInput
    }),
  })
    .then(response => response.json())
    .then(data => {
      console.log(data.answer, data.link);

      hideLoadingAnimation();

      displayOutput(userInput, data);
    })
    .catch(error => {
      console.error(error);
      hideLoadingAnimation();
      displayOutput(userInput, "Error occurred.");
    });
});

function displayOutput(input, response) {
  let inputElement = document.createElement("div");
  inputElement.classList.add("input-box");
  inputElement.textContent = input;
  outputContainer.appendChild(inputElement);

  let responseElement = document.createElement("div");
  responseElement.classList.add("response-box");

  let answerElement = document.createElement("div");
  answerElement.textContent = response.answer;
  responseElement.appendChild(answerElement);

  if (response.link) {
    let linkElement = document.createElement("a");
    linkElement.href = response.link;
    linkElement.textContent = response.link;
    linkElement.target = "_blank";

    let moreInfoElement = document.createElement("p");
    moreInfoElement.textContent = "For more information, follow this link: ";
    moreInfoElement.appendChild(linkElement);

    responseElement.appendChild(moreInfoElement);
  }

  outputContainer.appendChild(responseElement);
}

function showLoadingAnimation() {
  let loadingElement = document.createElement("div");
  loadingElement.classList.add("loading-animation");
  loadingElement.innerHTML = '<div class="dot"></div><div class="slash">/</div>';
  outputContainer.appendChild(loadingElement);
}

function hideLoadingAnimation() {
  let loadingElement = document.querySelector(".loading-animation");
  if (loadingElement) {
    outputContainer.removeChild(loadingElement);
  }
}
