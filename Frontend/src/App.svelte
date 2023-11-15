<script>

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
    <form>
      <input type="text">
      <button>Submit</button>
    </form>
    <table>
      <tr>
        <td>0</td>
        <td>0</td>
        <td>0</td>
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
    padding: 12px;
  }

  #body-container {
    margin: 12px;
  }

  #container {
    border: 1px solid gray;
    border-radius: 12px;
    padding: 12px;
  }
</style>
