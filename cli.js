import program from 'commander'

const customHelp = () => {
  console.log(`Examples:

    $ babel-node cli.js create --lat 45 --lng 90 --zoom 10
    `)
}

const validateOptions = (options) => {
  ['lat', 'lng', 'zoom'].map(field => {
    if (!options[field]) {
      console.error(`[ERROR] --${ field } is missing.`)
      process.exit(1)
    }
  })
}

const within = (value, { minValue, maxValue, parser, description }) => {
  value = parser(value)
  if (value >= minValue && value <= maxValue) return value
  console.error(`[ERROR] ${ description } must be within [${ minValue } | ${ maxValue }]`)
  process.exit(1)
}

program
  .version('0.0.1')
  .command('create')
  .description('Creates Kratelabs image from Mapbox\'s static API')
  .option('--filename <path>', 'Filename output to SVG')
  .option('--folder [path]', 'Folder output to SVG')
  .option('--location [location]', 'Geographical Location based on Google Maps')
  .option('--lat <float>',
          'latitude for the center point of the static map; number between  -90 and  90',
          value => within(value, {
            minValue: -90,
            maxValue: 90,
            parser: parseFloat,
            description: '--lat'
          }))
  .option('--lng, <float>',
          'longitude for the center point of the static map; number between  -180 and  180',
          value => within(value, {
            minValue: -180,
            maxValue: 180,
            parser: parseFloat,
            description: '--lng'
          }))
  .option('--zoom <float>',
          'zoom level; number between  0 and  22 . Fractional zoom levels will be rounded to two decimal places.',
          value => within(value, {
            minValue: 0,
            maxValue: 22,
            parser: parseFloat,
            description: '--zoom'
          }))
  .option('--width [int]',
          'Width of the image in pixels',
          value => within(value, {
            minValue: 0,
            maxValue: 1280,
            parser: parseInt,
            description: '--width'
          }),
          1280)
  .option('--height [int]',
          'Height of the image in pixels',
          value => within(value, {
            minValue: 0,
            maxValue: 1280,
            parser: parseInt,
            description: '--height'
          }),
          1280)
  .option('--style [style]',
          'mapbox://styles/{username}/{style_id}',
          'mapbox://styles/addxy/ciq40e6zx0010bkmbbo513b6s')
  .option('--access_token [token]',
          'Mapbox access token',
          'pk.eyJ1IjoiYWRkeHkiLCJhIjoiY2lsdmt5NjZwMDFsdXZka3NzaGVrZDZtdCJ9.ZUE-LebQgHaBduVwL68IoQ')
  .option('--bearing [float]',
          'Rotates the map around its center. Number between 0 and 360.',
          value => within(value, {
            minValue: 0,
            maxValue: 360,
            parser: parseFloat,
            description: '--bearing'
          }),
          0)
  .option('--pitch [float]',
          'Tilts the map, producing a perspective effect. Number between 0 and 60.',
          value => within(value, {
            minValue: 0,
            maxValue: 60,
            parser: parseFloat,
            description: '--tilt'
          }),
          0)
  .option('--retina [boolean]',
          'If  @2x is added to request a retina 2x image will be returned',
          Boolean,
          true)
  .option('--attribution [boolean]',
          'Value controlling whether there is attribution on the image; defaults to  false',
          Boolean,
          false)
  .option('--logo [boolean]',
          'Value controlling whether there is a Mapbox logo on the image; defaults to  false',
          Boolean,
          false)
  .on('--help', customHelp)
  .action((options) => {
    validateOptions(options)
    console.log('complete')
  })

program.parse(process.argv)
if (!program.args.length) program.help()
