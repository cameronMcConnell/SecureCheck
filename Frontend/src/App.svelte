<script>
  import { onMount } from 'svelte';

  // Used to determine what to return for the UI (Password Quality).
  const statusMap = {0: 'Weak', 1: 'Medium', 2: 'Strong'};

  // Used to determine what color to render for the table.
  const colorMap = {0: 'red', 1: 'yellow', 2: 'green'}

  // Used to show the quality in the UI. Updated after fetch.
  let passwordQuality = '';

  // Used to bind the table data to variables.
  let cell1;
  let cell2;
  let cell3;

  // Handle submit, send fetch request to get classification.
  const handleSubmit = async (event) => {
    // Reset UI.
    let tableDataElements = [cell1, cell2, cell3];
    let tableDataSubarrays = [tableDataElements.slice(0,1),tableDataElements.slice(0,2), tableDataElements.slice(0,3)];

    passwordQuality = '';
    tableDataElements.forEach((element) => element.style['background-color'] = 'white');

    // Format the event data.
    const formData = new FormData(event.target);
    
    // I hate this, it is dumb.
    let postData = {};
    for (let field of formData)
      postData[field[0]] = field[1]

    // Fetch predictions.
    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(postData)
    });

    const data = await response.json();

    // Update UI elements.
    passwordQuality = statusMap[data.prediction];
    tableDataSubarrays[data.predict].forEach((element) => element.style['background-color'] = colorMap[data.predict]);
  }
</script>

<main id='container'>
  <header>
    <h1>SecureCheck</h1>
  </header>
  <main id='body-container'>
    <p>
      SecureCheck uses machine learning to predict if your
      password is strong, given passwords procurred from a website leak
      and rated using Georgia Tech's PARS.
    </p>
    <form on:submit|preventDefault={handleSubmit}>
      <input type="password" name='data'>
      <button type="submit">Submit</button>
    </form>
    <p id='table-header'>Password Quality: {passwordQuality}</p>
    <table>
      <tr>
        <td bind:this={cell1}></td>
        <td bind:this={cell2}></td>
        <td bind:this={cell3}></td>
      </tr>
    </table>
  </main>
  <footer>

  </footer>
</main>

<style>
  h1 {
    text-align: center;
    margin: 12px;
  }

  form {
    display: flex;
    justify-content: center;
    margin: 12px;
    column-gap: 4px;
  }

  button:hover {
    cursor: pointer;
  }

  table, td {
    border: 1px solid black;
    border-collapse: collapse;
  }

  td {
    padding: 16px;
  }

  #table-header {
    margin-bottom: 6px;
  }

  #body-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    margin: 12px;
  }

  #container {
    border: 1px solid gray;
    border-radius: 12px;
    padding: 12px;
  }
</style>
