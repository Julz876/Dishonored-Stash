# 🚀 Blender Remote Asset Library Template

A turnkey starter template for hosting free, self-updating remote asset libraries for **Blender 5.2+** using **GitHub Pages**.

---

## 🛠️ Quick Start Guide (For Creators)

### 1. Generate Your Repository
Click the green **"Use this template"** button above to create a copy under your own GitHub account.

### 2. Configure Your Library
1. Clone your new repository locally:
   ```bash
   git clone [https://github.com/](https://github.com/)<YOUR-USERNAME>/<YOUR-REPO-NAME>.git
   cd <YOUR-REPO-NAME>
   ```

2. Add your `.blend` files into the `assets/` subfolders (`assets/Materials/`, `assets/GeometryNodes/`, `assets/Models/`, etc.).
   > **Note:** Always enable **File → External Data → Automatically Pack Resources** inside Blender before saving so textures and embedded dependencies are bundled properly.

3. Run the generator script to index files and render preview thumbnails:
   ```bash
   python publish.py
   ```
   *(Or press **`Ctrl + Shift + B`** in VS Code to run the pre-configured build task).*

### 3. Enable GitHub Pages
1. Go to your repository on GitHub and navigate to **Settings → Pages**.
2. Under **Build and deployment → Source**, select **Deploy from a branch**.
3. Choose branch **`main`** and folder **`/(root)`**, then click **Save**.
4. Your live library URL will be:
   ```text
   https://<YOUR-USERNAME>.github.io/<YOUR-REPO-NAME>/
   ```

---

## 📥 How to Install in Blender (For Users)

Share these steps with anyone who wants to connect to your library:

1. In Blender 5.2+, go to **Edit → Preferences → Asset Libraries**.
2. Click the **`+`** icon at the top right of the table and select **Add Remote Asset Library**.
3. Enter your library details:
   * **Name:** `<Your Library Name>`
   * **URL:** `https://<YOUR-USERNAME>.github.io/<YOUR-REPO-NAME>/`
4. Open the **Asset Browser** editor window (or press `Shift + F1`) and select your library from the top-left dropdown.

---

## ⚙️ Recommended Import Method: **Append**

When pulling assets into a scene:
* Set the **Import Method** in the Asset Browser header to **`Append`** (or **`Append (Reuse Data)`**).
* **Why?** Remote assets stream on demand. Using **Append** brings an independent, fully editable copy of shader graphs, Geometry Node trees, and mesh data directly into the active project file, preventing broken links if the scene is moved or shared.

---

## 📂 Repository Structure

```text
blender-remote-template/
├── .vscode/
│   └── tasks.json              # VS Code 1-click build shortcut (Ctrl + Shift + B)
├── assets/
│   ├── GeometryNodes/          # Modifiers & procedural node rigs (.blend)
│   ├── Materials/              # Shaders & surface setups (.blend)
│   ├── Models/                 # Props, kits, and assemblies (.blend)
│   └── Brushes/                # Sculpt & texture brushes (.blend)
├── .gitignore                  # Blocks .blend1 backup files & OS cache
├── .nojekyll                   # Forces GitHub Pages to serve underscore folders (_v1)
├── index.html                  # Landing page for web browser visitors
├── publish.py                  # Headless Blender index generator & git sync
└── README.md
```

> **Note:** The `publish.py` generator scans recursively across the entire project. You can add custom subfolders (e.g., `assets/HDRIs/`, `assets/Compositing/`) to match your workflow.