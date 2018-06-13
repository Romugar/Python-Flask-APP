    $(document).ready(function() {
    $('#resultado_busqueda').DataTable( {
        dom: 'Bfrtip',
        paging: false,
        "searching": false,
        "info": false,
        buttons: [
            'copyHtml5',
            'excelHtml5',
            'csvHtml5',
            'pdfHtml5'
        ]
    } );
} );