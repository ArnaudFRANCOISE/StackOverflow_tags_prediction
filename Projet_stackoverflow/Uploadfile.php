<?php
// Vérifier si le formulaire a été soumis
if($_SERVER["REQUEST_METHOD"] == "POST"){
    // Vérifie si le fichier a été uploadé sans erreur.
    if($_FILES["monfichier"]["error"] == 0){
       echo $_FILES["monfichier"]["name"];
        // Vérifie si le fichier existe avant de le télécharger.
        if(file_exists("upload/" . $_FILES["monfichier"]["name"])){
            echo $_FILES["monfichier"]["name"] . " existe déjà.";
        } else{
            move_uploaded_file($_FILES["monfichier"]["tmp_name"], "upload/" . $_FILES["monfichier"]["name"]);
            echo "Votre fichier a été téléchargé avec succès.";
        }
       
    } else{
        echo "Error: " . $_FILES["monfichier"]["error"];
    }
}
?>