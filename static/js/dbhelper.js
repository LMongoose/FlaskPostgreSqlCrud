
$(".table_create").click(function() {
    var $table = $("#tablename").text()
    var $id = $(this).closest("tr").find(".table_id_field").text();
    document.cookie = "table_name=" + $table;
    document.cookie = "selected_id=" + null;
});

$(".table_edit").click(function() {
    var $table = $("#tablename").text()
    if($table == "Animeography" || $table == "Staff")
    {
        var $id = $(this).closest("tr").find(".table_id_field").text();
        var $id2 = $(this).closest("tr").find(".table_id_field2").text();
        document.cookie = "table_name=" + $table;
        document.cookie = "selected_id=" + $id;
        document.cookie = "selected_id2=" + $id2;
    }
    else
    {
        var $id = $(this).closest("tr").find(".table_id_field").text();
        document.cookie = "table_name=" + $table;
        document.cookie = "selected_id=" + $id;
        document.cookie = "selected_id2=" + -1;
    }
});

$(".table_delete").click(function() {
    var $table = $("#tablename").text()
    if($table == "Animeography" || $table == "Staff")
    {
        var $id = $(this).closest("tr").find(".table_id_field").text();
        var $id2 = $(this).closest("tr").find(".table_id_field2").text();
        document.cookie = "table_name=" + $table;
        document.cookie = "selected_id=" + $id;
        document.cookie = "selected_id2=" + $id2;
    }
    else
    {
        var $id = $(this).closest("tr").find(".table_id_field").text();
        document.cookie = "table_name=" + $table;
        document.cookie = "selected_id=" + $id;
        document.cookie = "selected_id2=" + -1;
    }
});