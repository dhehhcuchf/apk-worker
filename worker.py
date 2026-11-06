<?php
include 'config.php';
header('Content-Type: application/json');

$action = $_GET['action'] ?? '';

if ($action === 'get_task') {
    $res = $connect->query("SELECT * FROM get_build_apk WHERE status = 'pending' ORDER BY created_at ASC LIMIT 1");
    if ($res && $row = $res->fetch_assoc()) {
        // قفل کردن تسک که دوباره خونده نشه
        $connect->query("UPDATE get_build_apk SET status = 'building' WHERE port = '{$row['port']}'");
        echo json_encode(['status' => 'success', 'data' => $row]);
    } else {
        echo json_encode(['status' => 'empty']);
    }
    exit;
}

if ($action === 'update_status') {
    $port = $_GET['port'] ?? '';
    $status = $_GET['status'] ?? '';
    if ($port && $status) {
        $connect->query("UPDATE get_build_apk SET status = '$status' WHERE port = '$port'");
        echo json_encode(['status' => 'updated']);
    }
    exit;
}
?>
