<!doctype html>
<html>
    <body>

    <?php
    $myDirectory = opendir(".");
    while($entryName = readdir($myDirectory)) {
        $dirArray[] = $entryName;
    }
    closedir($myDirectory);

    for($index=0; $index < count($dirArray); $index++) {
            $extension = substr($dirArray[$index], -3);
            if ($extension == 'jpg'){ 
                    echo "<a href=\"$dirArray[$index]\">$dirArray[$index]</a><br>";
            }    
    }
    ?>
</body>
</html>

