# New Features Documentation

## 1. Global Content Capture (Ctrl+Alt+A)

A new global hotkey `Ctrl+Alt+A` has been implemented to capture content from other applications and bring it directly into the AI Chat.

### How it works:
1.  **Select & Copy**: Copy text, images, or files in any other application (Browser, File Explorer, etc.) to your system clipboard.
2.  **Trigger**: Press `Ctrl+Alt+A` anywhere in your system.
3.  **Action**:
    *   Antigravity AI IDE comes to the foreground.
    *   The content is automatically formatted and inserted into the AI Chat input.
    *   **Text**: Inserted as text message.
    *   **Images**: Attached as image files (screenshots, copied images).
    *   **Files**: Formatted as a list of files for analysis.

### Requirements:
*   Requires `pynput` library (added to `requirements.txt`).
*   Requires `pillow` for image handling.
*   Works across Windows (optimized), macOS, and Linux.

## 2. Agent Group Library

Manage your AI agents more effectively with the new Agent Group Library.

*   **Access**: Click "📚 Lib" in the Agent Manager panel.
*   **Features**:
    *   Browse pre-configured agent groups (Dev Team, Research, Creative, etc.).
    *   Filter by category or search by name.
    *   Import groups directly into your active session.

## 3. Prompt Optimization Controls

Enhance your prompts before sending them to the AI.

*   **Access**: Click the "⚙️" icon in the AI Chat panel.
*   **Controls**:
    *   **Style**: Standard, Professional, Creative, Concise.
    *   **Complexity**: Beginner, Intermediate, Advanced.
    *   **Context**: Toggle context awareness.
*   **Effect**: Automatically injects system instructions to tailor the AI's response style.

## 4. Code Optimization Toolbar

Refactor and optimize your code with one click.

*   **Access**: Open any code file in the editor.
*   **Toolbar**: Located at the top of the editor.
*   **Modes**:
    *   **Performance**: Optimize for speed and efficiency.
    *   **Readability**: Improve code structure and comments.
    *   **Compact**: Reduce code size.
*   **Actions**:
    *   **Minify**: Remove whitespace/comments.
    *   **Optimize Code**: Sends the current code to the AI with the selected optimization instructions.

## 5. Troubleshooting

### Global Hotkey Not Working?
*   Ensure `pynput` is installed: `pip install pynput`
*   Check terminal logs for "Global Hotkey Listener Started".
*   On Linux/macOS, you may need to grant accessibility permissions to the IDE.

### Startup Errors?
*   If you see "NameError: name 'controls_row' is not defined", update `gui/ai_panel.py` or pull the latest changes. (Fixed in this update).
