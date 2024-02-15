<?php

$ch = curl_init('https://coderbyte.com/api/challenges/json/age-counting');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HEADER, 0);
$data = curl_exec($ch);
curl_close($ch);

$response = json_decode($data, true);

$count = 0;

if (isset($response['data'])) {
    $items = explode(", ", $response['data']);
    foreach ($items as $item) {
        $age = intval(preg_replace("/[^0-9]/", '', $item));
        if ($age >= 50) {
            $count++;
        }
    }
}

echo $count;

?>
