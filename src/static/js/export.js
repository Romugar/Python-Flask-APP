    $(document).ready(function() {
    $('#resultado_busqueda').DataTable( {
        dom: 'Bfrtip',
        paging: false,
        "searching": false,
        "info": false,
        buttons: [
            {
                extend: 'excel',
                text: 'EXPORTAR A EXCEL'
            }
        ]
    } );
} );