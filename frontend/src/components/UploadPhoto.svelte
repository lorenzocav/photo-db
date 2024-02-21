<script>
    let photoFile;
    let accountId = null;
    
    export let photoURL;
    export let fetchPhotos;
  
    async function uploadPhoto() {
      if (!photoFile) {
        alert("Please select a photo.");
        return;
      }
  
      if (!accountId || isNaN(accountId) || !Number.isInteger(Number(accountId))) {
        alert("Please enter a valid integer account ID.");
        return;
      }
  
      const formData = new FormData();
      formData.append("photo", photoFile);
  
      try {
        const response = await fetch(photoURL + `/?account_id=${accountId}`, {
          method: "POST",
          body: formData
        });
  
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.detail[0].msg);
        } else {
          fetchPhotos()
        }
  
        // alert("Photo uploaded successfully");
        
        // Reset the file input after successful upload
        photoFile = null;
        accountId = null;
        // Reset the input file
        const fileInput = document.getElementById('fileInput');
      if (fileInput) {
        fileInput.value = '';
      }
      } catch (error) {
        alert("Error uploading photo: " + error.message);
      }
    }
</script>
  

<h2>Upload Photo</h2>
<input id="fileInput" type="file" on:change={(e) => { photoFile = e.target.files[0]; }} placeholder= "Select a photo!">
<input type="number" bind:value={accountId} placeholder="Enter account ID">
<button on:click={uploadPhoto}>Upload photo</button>
  


<style>
  h2 {
    color: #003366; /* Blu scuro per il titolo */
  }

  input[type="file"], input[type="number"] {
    padding: 5px;
    margin: 10px 0; /* Aggiunge spazio sopra e sotto gli input */
    border: 1px solid #007bff; /* Bordo blu */
    border-radius: 5px; /* Bordo arrotondato */
    font-size: 0.9rem; /* Riduce la dimensione del font */
    /* width: calc(100% - 12px); Adatta la larghezza al contenitore */
    box-sizing: border-box; /* Include padding e bordo nella larghezza totale */
    cursor: pointer; /* Cambia il cursore in una manina per l'input file */
  }

  input[type="file"]::file-selector-button, input[type="number"]:focus, input[type="file"]:focus {
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