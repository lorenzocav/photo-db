<!-- CreateAccount.svelte -->
<script>
  let newName = null;
  export let fetchAccounts;
  export let accountURL;

  const createAccount = async () => {
    if (!newName) {
      alert('Please insert a name');
      return ;
    }
    try {
      const response = await fetch(accountURL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: newName })
      });

      if (response.ok) {
        fetchAccounts(); // Refresh account list after creating new account
        newName = null; // Reset the input field
        console.log('Account created successfully');
        // alert('Account created successfully');
      } else {
        alert('Failed to create account');
        const errorData = await response.json();
        throw new Error(errorData.detail[0].msg);
      }
    } catch (error) {
      console.error('Error creating account:', error);
    }
    };
</script>
  
<h2>Create Account</h2>
<input type="text" bind:value={newName} placeholder="Enter account name">
<button on:click={createAccount}>Create Account</button>


<style>
  h2 {
    color: #003366; /* Blu scuro per il titolo */
  }

  input[type="text"] {
    padding: 5px;
    margin: 10px 0; /* Aggiunge spazio sopra e sotto l'input */
    border: 1px solid #007bff; /* Bordo blu per l'input */
    border-radius: 5px; /* Bordo arrotondato */
    font-size: 0.9rem; /* Riduce la dimensione del font per coerenza */
    /* width: calc(100% - 12px); Adatta la larghezza all'elemento genitore, considerando il padding e il bordo */
    box-sizing: border-box; /* Assicura che padding e bordo siano inclusi nella larghezza totale */
  }

  input[type="text"]:focus {
    border-color: #0056b3; /* Cambia il colore del bordo quando in focus */
    outline: none; /* Rimuove l'outline di default */
  }

  button {
    background-color: #d6d6d6; /* Grigio chiaro per il bottone */
    color: #333; /* Testo scuro per contrasto */
    border: 1px solid #ccc; /* Bordo leggermente più scuro */
    padding: 5px 10px; /* Padding ridotto */
    margin: 5px 0; /* Margini per distanziare dal testo o altri elementi */
    border-radius: 5px; /* Bordo arrotondato */
    cursor: pointer; /* Cambia il cursore in una manina */
    transition: background-color 0.3s; /* Transizione per il cambio di colore */
    font-size: 0.9rem; /* Riduce la dimensione del font per coerenza */
  }

  button:hover {
    background-color: #bfbfbf; /* Grigio leggermente più scuro al passaggio del mouse */
  }
</style>
  