# MaterialDesignIcons-SCSS-Variables
This SCSS part file allows you to use [MaterialDesignIcons](https://github.com/Templarian/MaterialDesign)
project directly from your SCSS files.

Instead of using `<i class="mdi mdi-refresh"></i>`, you'll be able to style a button from SCSS:

    .icon-refresh {
        @include material-icon($mdi-refresh);
    }

## How to use this
Copy [`generated/_materialdesignicons.scss`](generated/_materialdesignicons.scss) & [`generated/_materialdesignicons-vars.scss`](generated/_materialdesignicons-vars.scss)
into your project, and import them in your scss file:

    # Import materialdesignicons variables
    @import 'materialdesignicons';
    @import 'materialdesignicons-vars';
    
    // Refresh icon
    .icon-refresh {
        @include material-icon($mdi-refresh);
    }

## How to update the vars list file

1. Download the Webfont from [materialdesignicons.com](https://materialdesignicons.com/)
2. Unzip the directory, and copy the `scss/_materialdesignicons.scss` file inside the `input/` directory
3. Run `python generate.py`
4. Enjoy `generated/_materialdesignicons-vars.scss`!
