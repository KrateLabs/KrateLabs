#! /usr/bin/env node
'use strict';

var _commander = require('commander');

var _commander2 = _interopRequireDefault(_commander);

var _shelljs = require('shelljs');

var _shelljs2 = _interopRequireDefault(_shelljs);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var customHelp = function customHelp() {
  console.log('Examples:\n\n    $ babel-node cli.js create --lat 45 --lng 90 --zoom 10\n    ');
};

var validateOptions = function validateOptions(options) {
  ['lat', 'lng', 'zoom'].map(function (field) {
    if (!options[field]) {
      console.error('[ERROR] --' + field + ' is missing.');
      process.exit(1);
    }
  });
};

var within = function within(value, _ref) {
  var minValue = _ref.minValue;
  var maxValue = _ref.maxValue;
  var parser = _ref.parser;
  var description = _ref.description;

  value = parser(value);
  if (value >= minValue && value <= maxValue) return value;
  console.error('[ERROR] ' + description + ' must be within [' + minValue + ' | ' + maxValue + ']');
  process.exit(1);
};

_commander2.default.version('1.0.0').command('create').description('Creates Kratelabs image from Mapbox\'s static API').option('--filename <path>', 'Filename output to SVG').option('--folder [path]', 'Folder output to SVG').option('--location [location]', 'Geographical Location based on Google Maps').option('--lat <float>', 'latitude for the center point of the static map; number between  -90 and  90', function (value) {
  return within(value, {
    minValue: -90,
    maxValue: 90,
    parser: parseFloat,
    description: '--lat'
  });
}).option('--lng, <float>', 'longitude for the center point of the static map; number between  -180 and  180', function (value) {
  return within(value, {
    minValue: -180,
    maxValue: 180,
    parser: parseFloat,
    description: '--lng'
  });
}).option('--zoom <float>', 'zoom level; number between  0 and  22 . Fractional zoom levels will be rounded to two decimal places.', function (value) {
  return within(value, {
    minValue: 0,
    maxValue: 22,
    parser: parseFloat,
    description: '--zoom'
  });
}).option('--width [int]', 'Width of the image in pixels', function (value) {
  return within(value, {
    minValue: 0,
    maxValue: 1280,
    parser: parseInt,
    description: '--width'
  });
}, 1280).option('--height [int]', 'Height of the image in pixels', function (value) {
  return within(value, {
    minValue: 0,
    maxValue: 1280,
    parser: parseInt,
    description: '--height'
  });
}, 1280).option('--style [style]', 'mapbox://styles/{username}/{style_id}', 'mapbox://styles/addxy/ciq40e6zx0010bkmbbo513b6s').option('--access_token [token]', 'Mapbox access token', 'pk.eyJ1IjoiYWRkeHkiLCJhIjoiY2lsdmt5NjZwMDFsdXZka3NzaGVrZDZtdCJ9.ZUE-LebQgHaBduVwL68IoQ').option('--bearing [float]', 'Rotates the map around its center. Number between 0 and 360.', function (value) {
  return within(value, {
    minValue: 0,
    maxValue: 360,
    parser: parseFloat,
    description: '--bearing'
  });
}, 0).option('--pitch [float]', 'Tilts the map, producing a perspective effect. Number between 0 and 60.', function (value) {
  return within(value, {
    minValue: 0,
    maxValue: 60,
    parser: parseFloat,
    description: '--tilt'
  });
}, 0).option('--retina [boolean]', 'If  @2x is added to request a retina 2x image will be returned', Boolean, true).option('--attribution [boolean]', 'Value controlling whether there is attribution on the image; defaults to  false', Boolean, false).option('--logo [boolean]', 'Value controlling whether there is a Mapbox logo on the image; defaults to  false', Boolean, false).on('--help', customHelp).action(function (options) {
  validateOptions(options);
  console.log('complete');
});

_commander2.default.parse(process.argv);
if (!_commander2.default.args.length) _commander2.default.help();