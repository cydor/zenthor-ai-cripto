#entrypoint.sh
#!/bin/sh
echo ">> Running in $ENV environment"

# Például: ha dev környezet, akkor verbose log, külön config, stb.
if [ "$ENV" = "dev" ]; then
    echo ">> Dev mode: debug logging enabled"
    exec python main.py --debug
elif [ "$ENV" = "prod" ]; then
    echo ">> Production mode: normal startup"
    exec python main.py
else
    echo ">> Unknown ENV=$ENV. Falling back to default run."
    exec python main.py
fi
exec "$@"  # --> ez futtatja a CMD-t (python main.py)