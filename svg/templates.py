TEMPLATES = {
    "PATH": "<path id=\"{element_id}\" d=\"{d}\" class=\"{style}\"/>",
    "LAYER": "<g id=\"{layer_id}\">{content}</g>",
    "CIRCLE": "<circle class=\"Plant\" id=\"{element_id}\" cx=\"{px}\" cy=\"{py}\" r=\"{diameter}\" /><text x=\"{px}\" y=\"{py}\" class=\"Caption\">{caption}</text>",
    "DOCUMENT": "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><svg width=\"{w}mm\" height=\"{h}mm\" viewBox=\"{x0} {y0} {x1} {y1}\" version=\"1.1\" id=\"{id}\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:svg=\"http://www.w3.org/2000/svg\"><style>{styles}</style>{content}</svg>"
}