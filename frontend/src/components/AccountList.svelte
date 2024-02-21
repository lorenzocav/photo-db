<!-- AccountList.svelte -->
<script>  
    export let accounts = [];
    export let accountURL;
    export let fetchAccounts;

    let newName = null;
    let activeAccountId = null; // Aggiunta variabile per tracciare l'ID dell'account attivo

    const deleteAccount = async (accountId) => {
      try {
        const response = await fetch(accountURL + `/${accountId}`, {
          method: 'DELETE'
        });
  
        if (response.ok) {
          fetchAccounts(); // Refresh account list after deleting
          console.log('Account deleted successfully');
          // alert('Account deleted successfully');
        } else {
          alert('Failed to delete account');
          const errorData = await response.json();
          throw new Error(errorData.detail[0].msg);
        }
      } catch (error) {
        console.error('Error deleting account:', error.message);
      }
    };

    const updateAccount = async (accountId) => {
      if (!newName){
        alert("Please insert an the new account's name.");
        return;
      }
    try {
      const response = await fetch(accountURL, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          id: accountId,
          name: newName
        })
      });

      if (response.ok) {
        fetchAccounts();
        console.log('Account updated successfully');
        toggleUpdateTextBox(accountId)
        // alert('Account updated successfully');
      } else {
        alert('Failed to create account');
        const errorData = await response.json();
        throw new Error(errorData.detail[0].msg); 
      }
    } catch (error) {
      console.error('Error updating account:', error.message);
      
    }
    };
    
    const toggleUpdateTextBox = (id) => {
    activeAccountId = (activeAccountId === id) ? null : id; // Toggle activeAccountId
    newName = null; // Reset newName when toggling
    };
</script>
  


<h2>Accounts List</h2>
<div class="grid-container">
  <div class="grid-item header">ID</div>
  <div class="grid-item header">Name</div>
  <div class="grid-item header">Actions</div>

  {#each accounts as account}
    <div class="grid-item">{account.id}</div>
    <div class="grid-item">{account.name}</div>
    <div class="grid-item action-container">
      <button on:click={() => toggleUpdateTextBox(account.id)}>Update</button>
      {#if activeAccountId === account.id}
        <input type="text" bind:value={newName} placeholder="Enter new name">
        <button on:click={() => updateAccount(account.id)}>Save</button>
      {/if}
      <button on:click={() => deleteAccount(account.id)}>Delete</button>
    </div>
  {/each}
</div>


<style>
  h2 {
    color: #003366; /* Mantiene il blu scuro per il titolo */
  }

  .grid-container {
    display: grid;
    grid-template-columns: auto auto 1fr; /* Adatta la dimensione delle prime due colonne al contenuto e usa lo spazio rimanente per le azioni */
    gap: 10px;
    align-items: center; /* Centra verticalmente gli elementi nella griglia */
  }

  .grid-item {
    background-color: #f0f8ff; /* Stile coerente con il resto dell'app */
    padding: 5px;
    border-radius: 5px;
    font-size: 0.9rem;
  }

  .header {
    font-weight: bold;
    background-color: transparent;
    padding-left: 5px;
  }

  .action-container {
    display: flex; /* Rende gli elementi delle azioni allineati orizzontalmente */
    gap: 5px; /* Spazio tra i bottoni e l'input */
  }
  
  button {
    background-color: #d6d6d6; /* Cambia il colore in grigio chiaro */
    color: #333; /* Testo scuro per contrastare con il grigio chiaro */
    border: 1px solid #ccc; /* Aggiunge un bordo leggermente più scuro */
    padding: 5px 10px; /* Riduce il padding per rendere i bottoni meno ingombranti */
    margin: 5px;
    border-radius: 5px; /* Mantiene i bordi arrotondati */
    cursor: pointer; /* Mantiene il cursore come manina */
    transition: background-color 0.3s; /* Mantiene la transizione per il cambio di colore */
  }

  button:hover {
    background-color: #bfbfbf; /* Un grigio leggermente più scuro al passaggio del mouse */
  }

  input[type="text"] {
    padding: 5px; /* Riduce il padding */
    margin: 5px 0; /* Mantiene lo spazio sopra e sotto l'input */
    border: 1px solid #007bff; /* Adatta il bordo all'aspetto ridotto */
    border-radius: 5px; /* Mantiene il bordo arrotondato */
    font-size: 0.9rem; /* Riduce la dimensione del testo per coerenza */
  }

  input[type="text"]:focus {
    border-color: #0056b3; /* Mantiene il cambio di colore al focus */
    outline: none; /* Mantiene l'outline rimosso */
  }
</style>

  