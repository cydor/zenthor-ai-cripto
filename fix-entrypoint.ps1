$entrypointContent = @"
#!/bin/sh
echo "🚀 ENTRYPOINT: környezet: \$ENV"

if [ "\$ENV" = "dev" ]; then
    echo ">> Dev mode: debug logging enabled"
    exec python main.py --debug
elif [ "\$ENV" = "prod" ]; then
    echo ">> Production mode: normal startup"
    exec python main.py
else
    echo ">> Unknown ENV=\$ENV. Falling back to default run."
    exec python main.py
fi
"@

[System.IO.File]::WriteAllText("entrypoint.sh", $entrypointContent)
Write-Host "`n✅ Új 'entrypoint.sh' fájl létrehozva. Teszteld a Docker buildet újra!" -ForegroundColor Green
