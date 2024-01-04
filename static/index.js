function displayresult(response) {
    console.log("generated");
    new Typewriter("#Example", {
      strings: response.data.answer,
      autoStart: true,
      delay: 1,
      cursor: "",
    });
  }
  
  function generate(event) {
    event.preventDefault();
  
    let instructionsInput = document.querySelector("#user-instructions");
    let apiKey = "ef5e3f47e22310b3ote67924e5d5ea4b";
    let prompt = `User instructions are: analyse the given sentence ${instructionsInput.value} so that person can know what is he feeling about `;
    let context =
      "You are a Psychologist here to find out the emotions and feelings of people to help them and console them. Also if they are not feelin well suggest them on how to overcome with it and suggest them the cure to go for it  in basic HTML and separate each line with a <br />. Make sure to follow the user instructions below. Do not include a title. Include a Signature with '- ai generated -' in a <strong> Element and <i> at the end of the poem.";
    let apiUrl = `https://api.shecodes.io/ai/v1/generate?prompt=${prompt}&context=${context}&key=${apiKey}`;
  
    let Element = document.querySelector("#Example");
    Element.innerHTML = `<div class="blink">Generating about ${instructionsInput.value} </div>`;
  
    console.log("Generating emotions and sense according to the sentence given");
    console.log(`Prompt is ${prompt}`);
    console.log(`Context is ${context}`);
  
    axios.get(apiUrl).then(displayresult);
  }
  
  let FormElement = document.querySelector("#form");
  FormElement.addEventListener("submit", generate);
  