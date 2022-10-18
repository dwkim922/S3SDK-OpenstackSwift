<?php
 
require 'C:\xampp\htdocs\aws\aws-autoloader.php';
 
// Establish connection to ZIOS with an S3 client.
$client = new Aws\S3\S3Client([
 'version' => 'latest',
 'region' => 'us-east-1',
 'endpoint' => '',
 'use_path_style_endpoint' => true,
 'credentials' => [
 'key' => '',
 'secret' => '',
 ]
]);
 
// List containers
$buckets = $client->listBuckets();
foreach ($buckets['Buckets'] as $bucket){
header('Content-type: text/plain');
echo "{$bucket['Name']}\r\n";
};


?>
