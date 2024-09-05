/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VCModelEnum } from './VCModelEnum';
export type VCImageGet = {
    /**
     * The unique code for the image
     */
    code: string;
    /**
     * The ML model for classifying vehicles
     *
     * * `EfficientNetB1` - EFFNETB1
     * * `YOLOv8s-cls` - YOLOV8SCLS
     */
    model?: VCModelEnum;
    /**
     * The uploaded image
     */
    image: string;
    /**
     * The inference time for the model
     */
    inf_time?: number;
    /**
     * The predicted class for the image
     */
    pred_class?: string;
};

