    $(document).ready(function() {
    $('#resultado_busqueda').DataTable( {
        dom: 'Bfrtip',
        paging: false,
        "searching": false,
        "info": false,
        buttons: [
            {
                extends: "excelHtml5",
                text: "EXPORTAR A EXCEL"
            }
        ]
    } );
} );