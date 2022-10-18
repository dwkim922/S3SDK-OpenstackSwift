
<?php

// require the AWS SDK for PHP library
//require 'aws-sdk-php/aws-autoloader.php';
require 'C:\xampp\htdocs\aws\aws-autoloader.php';
//use C:\xampp\htdocs\aws\S3Client;

// Establish connection to ZIOS with an S3 client.
$client = new Aws\S3\S3Client([
 'version' => 'latest',
 'region' => 'us-east-1',
 'endpoint' => 'https://vsa-00000004-kt-g-object-01.zadarazios.com',
 'use_path_style_endpoint' => true, // <---- 추가 기입 해주세요! 
 'credentials' => [
 'key' => 'ffa3c9a5c455472b8c8c88a74e7006e1',
 'secret' => '590804fe73db4b15b98c005c1de55eeb',
 ]
]);

// Send a PutObject request and get the result object.
$key = 'uploadingViaPHP.txt'; // <---- 오브젝트 이름
$result = $client->putObject([
	'Bucket' => 'tempurl',
	'Key'    => $key,
    'SourceFile' => 'uvp.txt', // <---- 업로드할 파일 경로 
	'ContentType' => 'abc/test' // <---- add custom header
]);

?>
