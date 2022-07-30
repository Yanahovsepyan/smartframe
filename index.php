<?php
error_reporting(-1);
ini_set('display_errors', 'On');
  $iamges = "<web>uploads/";
?>
<!Doctype html>
<html lang="en">
  <head>
    <h3 class = "id" style="margin-top: 15px ;" >Smart Frame</h3>
    <h6 style="text-align: center ; margin-top: 45px; "   >Here you can upload images , and uploaded images you will see in slide, if you don't want to see uploaded image in slide you can delete it from slide. </h6>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <style>
    
      .id{
        text-align: center;
      }
      .custom-file-input:lang(en)~.custom-file-label::after {
    content: "Browse";
    }
      
      .center {
        height:25%;
        display:flex;
        align-items:center;
        justify-content:center;

      }
      .image{
        position:relative;
        width: 370px;
        height: 300px;
      }
      .image>.delete:active{
        opacity: 0.8 !important;
        
      }
      .image > .delete{
        position: absolute;
        right: 115px ;
        top: 40px;
        width: 150px;
        height: 60px;
        z-index: 999999;
      }
    
      .image > .cancel{
        position: absolute;
        right: 115px ;
        bottom: 125px;
        width: 150px;
        height: 60px;
        z-index: 999999;
      }
      .image > img{
        position: absolute;
        top:0;
        left: 0px;
      }
      .custom-file-input ~ .custom-file-label::after {
          content: "Button Text";
      }
       </style>
    <title>Hello, world!</title>
  </head>
  <body>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <div class="upload-btn-wrapper">
  

</div>
<div class="container">
<!-- The Modal -->
<div class="modal" id="deletedModal">
  <div class="modal-dialog modal-sm">
    <div class="modal-content">

      <!-- Modal Header -->
      <div class="modal-header">
        <h4 class="modal-title">Image deleted</h4>
        <button type="button" class="close" data-dismiss="modal">&times;</button>
      </div>

      <!-- Modal body -->
      <div class="modal-body">
        Image deleted
      </div>

      <!-- Modal footer -->
      <div class="modal-footer">
        <button type="button" class="btn btn-warning" data-dismiss="modal">Close</button>
      </div>

    </div>
  </div>
</div>

  
<!-- The Modal -->
<div class="modal" id="myModal">
  <div class="modal-dialog">
    <div class="modal-content">

      <!-- Modal Header -->
      <div class="modal-header">
        <h4 class="modal-title">Image uploaded</h4>
        <button type="button" class="close" data-dismiss="modal">&times;</button>
      </div>

      <!-- Modal body -->
      <div class="modal-body">
        Image uploaded
      </div>

      <!-- Modal footer -->
      <div class="modal-footer">
        <button type="button" class="btn btn-warning" data-dismiss="modal">Close</button>
      </div>

    </div>
  </div>
</div>
  <div class="row">
    <div class="col">
      <div class="custom-file"> 
        <form action="upload.php" method="post" enctype="multipart/form-data" >
          <div class="input-group mb-3 px-2 py-2 rounded-pill bg-white shadow-sm" style="margin-top: 80px;" >
            <input id="upload"  style="padding: 0px;" type="file" name="fileToUpload"  onchange="readURL(this);"  class="form-control border-0">
            <div class="input-group-append">
              <input type="submit" class="btn btn-outline-secondary"  accept="image/png, image/gif, image/jpeg" data-toggle="modal" data-target="#myModal" value="Upload" name="submit">
            </div>
          </div>
          </div>
        </form>
      </div>  
    </div>
  </div>
</div>
<div class="container">
  <div class="row">

   
    
    <?php 
      $galleryDir = 'uploads/';
      foreach(glob("$galleryDir{*.jpg,*.png,*.jpeg}", GLOB_BRACE) as $photo)
      {echo '
        <div class="col-lg-4 col-md-12 mt-4 col">
        <div class="image  text-center "   >
          <img
            src="'.$photo.'"
            class="w-100 shadow-1-strong rounded mb-4"
            alt="Boat on Calm Water"
            onclick="addButtons(this, \''.$photo.'\')"
          />
        </div>
      </div>
              ';}
    ?>
  </div>
</div>
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
   

<script>
  <?php
    if(isset($_GET['image_deleted'])){
      echo "$('#deletedModal').modal('show');";
    }
  ?>
  
  var loc = window.location.pathname;
  var dir = loc.substring(0, loc.lastIndexOf('/'));

  function showPreview(event){
    if(event.target.files.length > 0){
      var src = URL.createObjectURL(event.target.files[0]);
      var preview = document.getElementById("file-ip-1-preview");
      preview.src = src;
      preview.style.display = "block";
    }
  }

  function showPreview(event){
    if(event.target.files.length > 0){
      var src = URL.createObjectURL(event.target.files[0]);
      var preview = document.getElementById("file-ip-1-preview");
      preview.src = src;
      preview.style.display = "block";
    }
  }

  function removeDummy() {
    var elems = document.getElementsByClassName('button');
    // elem.parentNode.removeChild(elem);
    for (const [key, value] of Object.entries(elems)) {
      value.remove();
    }
    
    return true;
  }
  
  function remove(image) {
    console.log(image);
    window.location.replace(dir +'/core.php?delete&image=' + image.split('/')[1] );
  }
  function addButtons(elem, image){
    elem.parentNode.innerHTML += `

      <button  type='button' id='delete1' class='mx-auto btn btn-danger col button text-xenter delete'  data-toggle="modal" data-target="deletedModal" onclick='remove("${image}")' >delete</button>  
      <button type='button'  class='mx-auto cancel  button btn btn-primary' id='cancel'  onclick='removeDummy()' >cancel</button> 
        
      `;
  }
</script>
      <p class="f" style= " text-align: center;  margin-top: 200px; "  > Created by: Ruben Petrosyan and Yana Hovsepyan with ❤️. </p>
  </body>
</html>