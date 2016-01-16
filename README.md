# Dropzone 3 Plugin For svg to React conversion

Plugin for [Aptonic's Dropzone 3](https://aptonic.com/dropzone3/). Converts svg to React component. It is very minimalistic and handles just one use case (mine).

### Features

- Handles [Sketch3](http://bohemiancoding.com/sketch/) default export
- Compresses it with [svgo](https://github.com/svg/svgo)
- Passes svg to [svg-to-jsx](https://github.com/janjakubnanista/svg-to-jsx)

### System requirements

- OS X (obviously)
- [Dropzone 3](https://aptonic.com/dropzone3/)
- svgo and svg-to-jsx installed with npm:

    `npm i -g svgo svg-to-jsx`
    
### Contributing

https://github.com/aptonic/dropzone3-actions/blob/master/README.md
