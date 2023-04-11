<template>
  <div class="upload">
    <p>讓我們來把你的照片變得更漂亮吧!</p>
    <input type="file" ref="fileInput" @change="previewImage">
    <br><br>
    <div v-if = "imageUrl">
      <img :src="imageUrl" style="max-width: 300px;">
    </div>
    <br><br>
    <button @click="uploadImage">上傳照片</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      file: null,
      imageUrl:null,
    };
  },
  methods: {
    previewImage(){
      const file = this.$refs.fileInput.files[0];
      this.file = file;
      this.imageUrl = URL.createObjectURL(file);
    },
    uploadImage(){
      const formData = new FormData();
      formData.append('file',this.file);
      axios.post('/api/upload',formData)
        .then((res) => {
          console.log("Success");
          console.log(res.data);
        })
        .catch((error) => {
          console.log("Fuck up")
          console.log(error)
        });
    }
  }
}
</script>
