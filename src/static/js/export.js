    $(document).ready(function() {
    $('#resultado_busqueda').DataTable( {
        dom: 'Bfrtip',
        paging: false,
        "searching": false,
        "info": false,
        buttons: [
            'excelHtml5'
        ]
    } );
} );