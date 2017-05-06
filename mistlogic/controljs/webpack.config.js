module.exports = {
    entry: './source/index.js',
    output: {
	filename: 'index.js',
	path: '../front-end/Mist/static/js/'
    },
    module: {
	loaders: [
	    {
		test: /\.js$/,
		exclude: /node_modules/,
		loader: 'babel-loader',
		query:{
		    presets: ['es2016']
		}
	    }
	]
    },
    target: 'web'
};
