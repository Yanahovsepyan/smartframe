<?php
// $b = array();
// file_put_contents('deleted.php',  '<?php return ' . var_export($b, true) . ';');

function getDeletedImages(){
    return include 'deleted.php';
}

function getUploadedImages(){
    return include 'uploaded.php';
}

if(isset($_GET['delete']) && isset($_GET['image'])){
    unlink("uploads/" . $_GET['image']);

    $images = getDeletedImages();
    array_push($images, $_GET['image']); 
    file_put_contents('deleted.php',  '<?php return ' . var_export($images, true) . ';');
    header("Location: index.php?image_deleted");
}
if(isset($_GET['getUploadedImages'])){
    echo json_encode(getUploadedImages());
    file_put_contents('uploaded.php',  '<?php return ' . var_export(array(), true) . ';');
}
