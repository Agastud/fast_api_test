import uvicorn


def main() -> None:
    uvicorn.run('application:get_app', host='localhost', port=8000, reload=True, factory=True)


if __name__ == '__main__':
    main()
