# Guess Lyrics By Genre
Version: 0.1.0

An attempt to guess a song's genre by its lyrics, using ML models

## Getting Started

### Prerequisites
* Anaconda for Python 2 or Python 3
* fuzzywuzzy
* python-Levenshtein


### Installing

```
git clone https://github.com/ormatt/Guess-Lyrics-By-Genre.git
python setup.py install
```

## Usage

Run this line to start the application

Train and test a model:
```
$ python ./build_model.py [--train] [--test] [--verbosity {debug,info,critical}]
```
Make predictions based on a built model:
```
$ python ./make_prediction.py
```

### Jupyter Notebook ### 
A Jupyter Notebook, *GuessGenreByLyrics.ipynb*,  is provided for quick prototyping.

## Contributing

If you would like to contribute, please send a pull request against the master branch.


## Authors

* **OrMatt** - *Initial work* -  [OrMatt](https://github.com/ormatt)
* **Matt Murch** - *Initial work* - [Matt Murch](https://github.com/mattmurch)

## License

This project is licensed under the GPL - 3.0 License - see the [LICENSE](LICENSE) file for details


## Acknowledgments
