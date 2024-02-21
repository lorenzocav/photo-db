<!-- App.svelte -->
<script>
  // Imports
  import { onMount } from 'svelte';
  import Header from './components/Header.svelte';
  import Footer from './components/Footer.svelte';
  import Tabs from './shared/Tabs.svelte';
  import AccountList from './components/AccountList.svelte';
  import CreateAccount from './components/CreateAccount.svelte';
  import PhotoUploader from './components/UploadPhoto.svelte';
  import PhotoList from './components/PhotoList.svelte';
  
  // Variables
  let accounts = [];
  let photos = [];
  let baseURL = 'http://localhost:8000/'
  let accountURL = baseURL + 'account'
  let photoURL = baseURL + 'photo'
  
  // Tabs
  let items = ['Accounts', 'Photos']
  let activeItem = 'Accounts'
  const tabChange = (e) =>{
		activeItem = e.detail;
	}

  // Fetching Functions
  const fetchAccounts = async () => {
    try {
      const response = await fetch(baseURL + 'accounts');
      if (!response.ok){
        const errorData = await response.json();
        throw new Error(errorData.detail[0].msg);
      }

      accounts = await response.json();
    } catch (error) {
      console.error('Error fetching accounts:', error);
      alert('Error fetching the accounts: ' + error.message)
    }
    };

  const fetchPhotos = async () => {
    try {
      const response = await fetch(baseURL + 'photos');
      if (!response.ok){
        const errorData = await response.json();
        throw new Error(errorData.detail[0].msg);
      }

      photos = await response.json();
    } catch (error) {
      console.error('Error fetching photos:', error);
      alert('Error fetching the photos: ' + error.message)
    }
    };
  
    onMount(fetchAccounts);
    onMount(fetchPhotos);
</script>
 
<Header />
<main>
  <Tabs items = {items} activeItem = {activeItem} on:TabChange={tabChange}/>
  {#if activeItem === 'Accounts'}
    <AccountList {accounts} {accountURL} {fetchAccounts} />
    <CreateAccount {accountURL} {fetchAccounts} />
  {:else if activeItem === 'Photos'}
    <PhotoList {photos} {photoURL} {fetchPhotos} />
    <PhotoUploader {photoURL} {fetchPhotos}/>
  {/if}
</main>
<Footer />


<style>
	main{
		max-width: 960px;
		margin:40px auto;
	}
</style>
  