<!DOCTYPE html>
<html>
<head>
<title>Image Upload</title>
<style>
  body {
    margin:0px;
  }

  .center {
    display:inline;
    margin: 3px;
  }

  /* This is the dotted blue box around the upload image  */
  .form-input {
    width: 300px;
    height: 300px;
   /* padding:3px; */
    background:#fff;
    border:2px dashed dodgerblue;
  }
 
  .form-input input {
    display:none;
  }

  /* This is the size of the gray box around the upload icon 
  .form-input label {
    display:block;
    width: 300px;
    height: auto;
    max-height: 300px;
    background:#333;
    border-radius:10px;
    cursor:pointer;
  }
  */ 

  /* This is the actual size of the image when it is uploaded  (remember .4 for opacity*/
  .form-input img {
    width: 300px;
    height: 300px;
    margin: 2px;
    opacity: 1;
  }

  /* Moves the reset/remove icon */ 
  .imgRemove{
    position: relative;
    bottom: 114px;
    left: 70%;
    background-color: transparent;
    border: none;
    font-size: 30px;
    outline: none;
  }
  .imgRemove::after{
    content: ' \21BA';
    color: #fff;
    font-weight: 900;
    border-radius: 8px;
    cursor: pointer;
  }
  .small{
    color: firebrick;
  } 
  </style>

</head>

<body>

   <div class="image-upload-one">
     <div class="center">
       <div class="form-input">
         <label for="file-ip-1">
           <img id="file-ip-1-preview" src="https://i.ibb.co/ZVFsg37/default.png">
           <button type="button" class="imgRemove" onclick="myImgRemoveFunctionOne()"></button>
         </label>
         <input type="file"  name="img_one" id="file-ip-1" accept="image/*" onchange="showPreviewOne(event);">
       </div>
       <small class="small"> Click on the space above to upload an image</small>
     </div>
   </div>
    
  <script>

    function showPreviewOne(event){
      if(event.target.files.length > 0){
        let src = URL.createObjectURL(event.target.files[0]);
        let preview = document.getElementById("file-ip-1-preview");
        preview.src = src;
        preview.style.display = "block";
      } 
    }
    function myImgRemoveFunctionOne() {
      document.getElementById("file-ip-1-preview").src = "https://i.ibb.co/ZVFsg37/default.png";
    }

  </script>
   
</body>
</html>