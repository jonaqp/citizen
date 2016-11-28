var path = require('path');

var app = require(path.resolve(__dirname, 'server/server'));
var ds = app.datasources.cnvDS;
ds.automigrate('Citizen', function (err) {
  if (err) throw err;

  var citizens = [
    {
      NUMERO_CNV: '17',
      TIPO_DOC_MADRE: '17',
      NUMERO_DOC_MADRE: '17'
    },
    {
      NUMERO_CNV: '16',
      TIPO_DOC_MADRE: '16',
      NUMERO_DOC_MADRE: '16'
    }
  ];
  var count = citizens.length;
  citizens.forEach(function (citizen) {
    app.models.Citizen.create(citizen, function (err, model) {
      if (err) throw err;

      console.log('Created:', model);

      count--;
      if (count === 0)
        ds.disconnect();
    });
  });
});
