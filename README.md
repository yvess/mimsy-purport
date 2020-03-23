# mimsy purport

wagtail headless multilanguage test

## install

First install poetry. 

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
```

Install virtual env and dependencies with poetry.

```bash
poetry install
```

Enter shell and setup project and run it.

```bash
poetry shell
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

Go to [admin](http://localhost:8000/admin/) and add some pages.

Make some queries in [graphql](http://localhost:8000/graphql/). 

```graphql
{
    pages {
        id
        contentType
        title
        slug
        url
        urlPath
        ...on HomePage {
            body {
                blockType
                field
                rawValue
            }
        }
        ...on ContentPage {
            layout
            body {
                blockType
                field
                rawValue
            }
        }
    }
}
```
