#!/bin/bash
echo "📂 Elérhető fájlok a config/ mappában:"
ls -l config/
echo "🧪 JSON tartalom (dev):"
cat config/dev.json

if [ ! -s config/dev.json ]; then
  echo "❌ A config/dev.json üres!" && exit 1
fi
