    $(document).ready(function() {
    $('#exportar_tabla').DataTable( {
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