<script>
    export let photos = [];
    export let photoURL;
    export let fetchPhotos;

    let selectedPhoto = null;

    // Funzione per aprire il popup
    function openPhotoPopup(photo) {
      selectedPhoto = photo;
    }

    // Funzione per chiudere il popup
    function closePhotoPopup() {
      selectedPhoto = null;
    }

    
    const deletePhoto = async (photoID) => {
        try{
            const response = await fetch(photoURL +`/${photoID}`, {
                method: 'DELETE'
            });
            if (response.ok){
                fetchPhotos();
                // alert('Photo deleted succesfully');
            } else{
                alert('Failed to delete photo');
                const errorData = await response.json();
                throw new Error(errorData.detail[0].msg);
            }

        } catch (error){
            console.error('Error deleting photo:', error.message);
        }
    };
</script>


<h2>Photos List</h2>
<div class="grid-container">
    <div class="grid-item header">ID</div>
    <div class="grid-item header">Title</div>
    <div class="grid-item header">User ID</div>
    <div class="grid-item header">Upload Date</div>
    <div class="grid-item header">Actions</div>

    {#each photos as photo}
        <div class="grid-item">{photo.id}</div>
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div class="grid-item title" on:click={() => openPhotoPopup(photo)}>{photo.photo_title}</div>
        <div class="grid-item">{photo.user_id}</div>
        <div class="grid-item">{photo.date_upload}</div>
        <div class="grid-item">
          <button on:click={() => deletePhoto(photo.id)}>Delete photo</button>
        </div>
    {/each}
</div>

{#if selectedPhoto}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <div class="overlay active" on:click={closePhotoPopup}></div>
  <div class="popup active">
    <h2>{selectedPhoto.photo_title}</h2>
    <!-- svelte-ignore a11y-img-redundant-alt -->
    <img src={`data:image/jpeg;base64,${selectedPhoto.photo_data_base64}`} alt="Photo Popup" />
    <button on:click={closePhotoPopup}>Close</button>
  </div>
{/if}


<style>
  h2 {
    color: #003366; /* Blu scuro per il titolo */
  }

  .grid-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr); /* Definisce 5 colonne di eguale dimensione */
  gap: 10px; /* Spazio tra gli elementi */
  }

  .grid-item {
    background-color: #f0f8ff; /* Un blu molto chiaro per lo sfondo degli elementi */
    padding: 3px; /* Padding per ogni elemento della griglia */
    border-radius: 5px; /* Bordo arrotondato */
    font-size: 0.8rem; /* Dimensione del testo */
  }

  .grid-item.title {
    cursor: pointer;
    color: #007bff; /* Colore blu per indicare che è cliccabile, ma puoi scegliere qualsiasi colore */
    text-decoration: underline; /* Sottolinea per indicare che è un link/cliccabile */
  }
  
  .grid-item.title:hover {
    color: #0056b3; /* Colore leggermente più scuro al passaggio del mouse */
  }

  .header {
    font-weight: bold; /* Rende il testo delle etichette grassetto */
    background-color: transparent; /* Rimuove lo sfondo per le etichette */
    padding-left: 5px; /* Allinea il padding con gli altri elementi della griglia */
  }

  button {
    background-color: #d6d6d6; /* Grigio chiaro per il bottone */
    color: #333; /* Testo scuro per contrasto */
    border: 1px solid #ccc; /* Bordo leggermente più scuro */
    padding: 5px 10px; /* Padding ridotto */
    margin: 5px; /* Margini per distanziare dal testo o altri elementi */
    border-radius: 5px; /* Bordo arrotondato */
    cursor: pointer; /* Cambia il cursore in una manina */
    transition: background-color 0.3s; /* Transizione per il cambio di colore */
    font-size: 0.9rem; /* Riduce la dimensione del font per coerenza */
  }

  button:hover {
    background-color: #bfbfbf; /* Grigio leggermente più scuro al passaggio del mouse */
  }

  .popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    z-index: 1000; /* Assicurati che sia al di sopra di altri contenuti */
    display: none;
  }
  .popup.active {
    display: block;
  }
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 999; /* Sotto il popup ma sopra altri contenuti */
    display: none;
  }
  .overlay.active {
    display: block;
  }
</style>